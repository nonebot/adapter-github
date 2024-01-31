from typing import TYPE_CHECKING

from . import lazy_module

lazy_module.apply()

if TYPE_CHECKING:
    from .event import *  # noqa: F403
else:
    from . import event

    def __getattr__(name: str):
        try:
            return getattr(event, name)
        except AttributeError:
            raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


from .bot import Bot as Bot
from .bot import OAuthBot as OAuthBot
from .adapter import Adapter as Adapter
from .bot import GitHubBot as GitHubBot
from .message import Message as Message
from .exception import ActionFailed as ActionFailed
from .exception import GraphQLError as GraphQLError
from .exception import NetworkError as NetworkError
from .exception import ActionTimeout as ActionTimeout
from .message import MessageSegment as MessageSegment
from .exception import GitHubAdapterException as GitHubAdapterException
