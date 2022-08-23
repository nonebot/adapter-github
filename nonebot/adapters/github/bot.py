from typing import TYPE_CHECKING, Union, Optional

from nonebot.typing import overrides
from nonebot.message import handle_event
from githubkit import GitHub, AppAuthStrategy, OAuthAppAuthStrategy

from nonebot.adapters import Bot as BaseBot

from .event import Event
from .config import OAuthApp, GitHubApp

if TYPE_CHECKING:
    from .adapter import Adapter


class Bot(BaseBot):
    github: GitHub

    @overrides(BaseBot)
    def __init__(self, adapter: "Adapter", app: Union[GitHubApp, OAuthApp]):
        super().__init__(adapter, app.id)
        self.app = app

    async def handle_event(self, event: Event) -> None:
        await handle_event(self, event)

    @overrides(BaseBot)
    async def send(self, event: Event, message):
        ...


class OAuthBot(Bot):
    @overrides(Bot)
    def __init__(self, adapter: "Adapter", app: OAuthApp):
        super().__init__(adapter, app)
        self._github = GitHub(OAuthAppAuthStrategy(app.client_id, app.client_secret))


class GitHubBot(Bot):
    @overrides(Bot)
    def __init__(self, adapter: "Adapter", app: GitHubApp):
        super().__init__(adapter, app)
        self._github = GitHub(
            AppAuthStrategy(
                app.app_id, app.private_key, app.client_id, app.client_secret
            )
        )
        self._app_slug: Optional[str] = None

    async def _get_self_info(self):
        res = await self._github.rest.apps.async_get_authenticated()
        self._app_slug = (
            slug if isinstance((slug := res.parsed_data.slug), str) else None
        )
