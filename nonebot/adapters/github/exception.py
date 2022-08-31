"""OneBot v11 错误类型。

FrontMatter:
    sidebar_position: 8
    description: onebot.v11.exception 模块
"""

from githubkit.exception import RequestFailed
from nonebot.exception import AdapterException
from nonebot.exception import ActionFailed as BaseActionFailed
from nonebot.exception import NetworkError as BaseNetworkError
from nonebot.exception import NoLogException as BaseNoLogException
from nonebot.exception import ApiNotAvailable as BaseApiNotAvailable


class GitHubAdapterException(AdapterException):
    def __init__(self):
        super().__init__("GitHub")


class NetworkError(BaseNetworkError, GitHubAdapterException):
    """网络错误。"""


class ApiNotAvailable(BaseApiNotAvailable, GitHubAdapterException):
    pass


class ActionFailed(RequestFailed, BaseActionFailed, GitHubAdapterException):
    def __repr__(self) -> str:
        return (
            f"<ActionFailed: {self.response.raw_request.method} "
            f"{self.response.raw_request.url}, status_code: {self.response.status_code}>"
        )
