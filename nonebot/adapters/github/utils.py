import re
import contextlib
from typing import TYPE_CHECKING, Any, Tuple

from nonebot.utils import logger_wrapper

if TYPE_CHECKING:
    from .bot import Bot

log = logger_wrapper("GitHub")


def escape(content: str) -> str:
    return re.sub(r"\\|`|\*|_|{|}|\[|\]|\(|\)|#|\+|-|\.|!", r"\\\1", content)


def get_attr_or_item(obj: Any, attr: str) -> Any:
    with contextlib.suppress(TypeError, KeyError):
        return getattr(obj, attr, None) or obj[attr]


class APIContext:
    __slots__ = ("bot", "parts")

    def __init__(self, bot: "Bot", parts: Tuple[str, ...]):
        self.bot = bot
        self.parts = parts

    def __getattr__(self, name: str) -> "APIContext":
        return APIContext(self.bot, self.parts + (name,))

    async def __call__(self, **kwargs: Any) -> Any:
        return await self.bot.call_api(".".join(self.parts), **kwargs)
