import json
import asyncio
import inspect
from functools import partial
from typing_extensions import override
from typing import Any, Type, Union, Callable, Optional, cast

from githubkit.webhooks import verify
from nonebot.compat import type_validate_python
from githubkit.exception import GraphQLFailed, RequestFailed, RequestTimeout
from nonebot.drivers import (
    URL,
    Driver,
    Request,
    Response,
    ReverseDriver,
    HTTPServerSetup,
)

from nonebot import get_plugin_config
from nonebot.adapters import Adapter as BaseAdapter

from . import event
from .utils import log
from .event import Event, events
from .bot import Bot, OAuthBot, GitHubBot
from .message import Message, MessageSegment
from .config import Config, OAuthApp, GitHubApp
from .exception import ActionFailed, GraphQLError, NetworkError, ActionTimeout


def import_event_model(event_name: str) -> Type[Event]:
    return getattr(event, event_name)


class Adapter(BaseAdapter):
    @override
    def __init__(self, driver: Driver, **kwargs: Any):
        super().__init__(driver, **kwargs)
        self.github_config = get_plugin_config(Config)
        self._setup()

    @classmethod
    @override
    def get_name(cls) -> str:
        return "GitHub"

    def _setup(self):
        if not isinstance(self.driver, ReverseDriver):
            log(
                "WARNING",
                f"Current driver {self.config.driver} is not a ReverseDriver. GitHub"
                " Webhook disabled.",
            )

        for app in self.github_config.github_apps:
            webhook_route = HTTPServerSetup(
                URL("/github/webhooks") / app.id,
                "POST",
                self.get_name(),
                partial(self._handle_webhook, app=app),
            )
            self.setup_http_server(webhook_route)

        self.driver.on_startup(self._startup)

    async def _startup(self):
        await asyncio.gather(
            *(self._startup_app(app) for app in self.github_config.github_apps)
        )

    async def _startup_app(self, app: Union[GitHubApp, OAuthApp]):
        if isinstance(app, GitHubApp):
            bot = GitHubBot(self, app)
            await bot._get_self_info()
        else:
            bot = OAuthBot(self, app)
        self.bot_connect(bot)

    async def _handle_webhook(
        self, request: Request, app: Union[GitHubApp, OAuthApp]
    ) -> Response:
        event_id = request.headers.get("x-github-delivery")
        event_name = request.headers.get("x-github-event")
        signature = request.headers.get("x-hub-signature-256")
        payload = request.content

        if not event_id or not event_name or not payload:
            log("WARNING", "Received invalid GitHub Webhook request. Missing Header.")
            return Response(400, content="Invalid Request")

        # verify signature
        if app.webhook_secret is not None and not (
            signature and verify(app.webhook_secret, payload, signature)
        ):
            log(
                "WARNING",
                "Received invalid GitHub Webhook request. Invalid Signature.",
            )
            return Response(400, content="Invalid Signature")

        if event := self.payload_to_event(event_id, event_name, payload):
            bot = cast(Bot, self.bots[app.id])
            asyncio.create_task(bot.handle_event(event))

        return Response(200, content="OK")

    async def _call_api(self, bot: Bot, api: str, **data: Any) -> Any:
        parts = api.split(".")
        func: Any = bot.github
        for part in parts:
            func = getattr(func, part)
        if not inspect.isroutine(func) or not inspect.iscoroutinefunction(func):
            raise TypeError(f"{api} is invalid.")

        try:
            return await func(**data)
        except RequestFailed as e:
            raise ActionFailed(e.response) from None
        except RequestTimeout as e:
            raise ActionTimeout(e.request) from None
        except GraphQLFailed as e:
            raise GraphQLError(e.response) from None
        except Exception as e:
            raise NetworkError(f"API request failed: {e!r}") from e

    @classmethod
    def payload_to_event(
        cls, event_id: str, event_name: str, payload: Union[str, bytes]
    ) -> Optional[Event]:
        event_payload = json.loads(payload)
        try:
            types = events.get(event_name)
            if isinstance(types, dict):
                if action := event_payload.get("action"):
                    return type_validate_python(
                        import_event_model(types[action]),
                        {
                            "id": event_id,
                            "name": event_name,
                            "payload": event_payload,
                        },
                    )
                else:
                    raise ValueError(
                        f"Payload missing action, either of {', '.join(types)}."
                    )
            elif types is None:
                raise ValueError(f"Unknown event type {event_name}.")
            return type_validate_python(
                import_event_model(types),
                {"id": event_id, "name": event_name, "payload": event_payload},
            )
        except Exception as e:
            log("WARNING", f"Failed to parse webhook payload {event_id}", e)
            return type_validate_python(
                Event, {"id": event_id, "name": event_name, "payload": event_payload}
            )

    @classmethod
    def custom_send(
        cls,
        send_func: Callable[[Bot, Event, Union[str, Message, MessageSegment]], Any],
    ):
        """自定义 Bot 的回复函数。"""
        Bot.send_handler = send_func
