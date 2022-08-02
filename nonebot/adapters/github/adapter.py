from functools import partial
from typing import Any, Union, Optional

from nonebot.typing import overrides
from githubkit.webhooks import parse, verify
from nonebot.drivers import (
    URL,
    Driver,
    Request,
    Response,
    ReverseDriver,
    HTTPServerSetup,
)

from nonebot.adapters import Adapter as BaseAdapter

from .utils import log
from .event import Event
from .config import Config, OAuthApp, GitHubApp


class Adapter(BaseAdapter):
    @overrides(BaseAdapter)
    def __init__(self, driver: Driver, **kwargs: Any):
        super().__init__(driver, **kwargs)
        self.github_config = Config.parse_obj(self.config)
        self._setup()

    @classmethod
    @overrides(BaseAdapter)
    def get_name(cls) -> str:
        return "GitHub"

    def _setup(self):
        if not isinstance(self.driver, ReverseDriver):
            log(
                "WARNING",
                f"Current driver {self.config.driver} is not a ReverseDriver. GitHub Webhook disabled.",
            )

        for app in self.github_config.github_apps:
            self_id = app.client_id if isinstance(app, OAuthApp) else app.app_id
            webhook_route = HTTPServerSetup(
                URL("/github/webhooks") / self_id,
                "POST",
                self.get_name(),
                partial(self._handle_webhook, app=app),
            )
            self.setup_http_server(webhook_route)

    async def _handle_webhook(
        self, request: Request, app: Union[OAuthApp, GitHubApp]
    ) -> Response:
        event_id = request.headers.get("x-github-delivery")
        event_name = request.headers.get("x-github-event")
        signature = request.headers.get("x-hub-signature-256")
        payload = request.content

        if not event_id or not event_name or not signature or not payload:
            log("WARNING", "Received invalid GitHub Webhook request. Missing Header.")
            return Response(400, content="Invalid Request")

        # verify signature
        if app.webhook_secret is not None and not verify(
            app.webhook_secret, payload, signature
        ):
            log(
                "WARNING",
                "Received invalid GitHub Webhook request. Invalid Signature.",
            )
            return Response(400, content="Invalid Signature")

        if event := self.payload_to_event(event_id, event_name, payload):
            self_id = app.client_id if isinstance(app, OAuthApp) else app.app_id
            bot = self.bots.get(self_id, None)

        return Response(200, content="OK")

    @classmethod
    def payload_to_event(
        cls, event_id: str, event_name: str, payload: Union[str, bytes]
    ) -> Optional[Event]:
        try:
            payload_event = parse(event_name, payload)
        except Exception as e:
            log("ERROR", f"Failed to parse webhook payload {event_id}", e)
