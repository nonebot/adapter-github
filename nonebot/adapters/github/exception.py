"""OneBot v11 错误类型。

FrontMatter:
    sidebar_position: 8
    description: onebot.v11.exception 模块
"""

from typing import Optional

from nonebot.exception import AdapterException
from nonebot.exception import ActionFailed as BaseActionFailed
from nonebot.exception import NetworkError as BaseNetworkError
from githubkit.exception import GraphQLFailed, RequestFailed, RequestTimeout


class GitHubAdapterException(AdapterException):
    def __init__(self):
        super().__init__("GitHub")


class NetworkError(BaseNetworkError, GitHubAdapterException):
    def __init__(self, msg: Optional[str] = None):
        super().__init__()
        self.msg: Optional[str] = msg
        """错误原因"""

    def __repr__(self):
        return f"NetWorkError(message={self.msg!r})"


class ActionTimeout(RequestTimeout, NetworkError): ...


class ActionFailed(RequestFailed, BaseActionFailed, GitHubAdapterException): ...


class GraphQLError(GraphQLFailed, BaseActionFailed, GitHubAdapterException): ...
