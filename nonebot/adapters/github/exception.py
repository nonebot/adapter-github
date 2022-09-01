"""OneBot v11 错误类型。

FrontMatter:
    sidebar_position: 8
    description: onebot.v11.exception 模块
"""

from typing import Optional

from nonebot.exception import AdapterException
from githubkit.exception import RequestFailed, RequestTimeout
from nonebot.exception import ActionFailed as BaseActionFailed
from nonebot.exception import NetworkError as BaseNetworkError
from nonebot.exception import ApiNotAvailable as BaseApiNotAvailable


class GitHubAdapterException(AdapterException):
    def __init__(self):
        super().__init__("GitHub")


class NetworkError(BaseNetworkError, GitHubAdapterException):
    def __init__(self, msg: Optional[str] = None):
        super().__init__()
        self.msg: Optional[str] = msg
        """错误原因"""

    def __repr__(self):
        return f"<NetWorkError message={self.msg}>"


class ActionTimeout(RequestTimeout, NetworkError):
    def __repr__(self) -> str:
        return f"<NetworkError: {self.request.method} {self.request.url}>"


class ApiNotAvailable(BaseApiNotAvailable, GitHubAdapterException):
    ...


class ActionFailed(RequestFailed, BaseActionFailed, GitHubAdapterException):
    def __repr__(self) -> str:
        return (
            f"<ActionFailed: {self.response.raw_request.method} "
            f"{self.response.raw_request.url}, status_code: {self.response.status_code}>"
        )
