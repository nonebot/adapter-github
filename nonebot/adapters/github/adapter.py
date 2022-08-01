from typing import Any

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
from .config import Config


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

        webhook_route = HTTPServerSetup(
            URL("/github/webhooks"), "POST", self.get_name(), self._handle_webhook
        )
        self.setup_http_server(webhook_route)

    async def _handle_webhook(self, request: Request) -> Response:
        event_id = request.headers.get("x-github-delivery")
        event_name = request.headers.get("x-github-event")
        signature = request.headers.get("x-hub-signature-256")
        payload = request.content

        if not event_id or not event_name or not signature or not payload:
            log("WARNING", "Received invalid GitHub Webhook request. Missing Header.")
            return Response(400, content="Invalid Request")

        # verify signature
        if self.github_config.webhook_secret is not None:
            if not verify(self.github_config.webhook_secret, signature, payload):
                log(
                    "WARNING",
                    "Received invalid GitHub Webhook request. Invalid Signature.",
                )
                return Response(400, content="Invalid Signature")

        return Response(200, content="OK")
