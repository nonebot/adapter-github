from functools import cached_property
from typing_extensions import override

from nonebot.compat import PYDANTIC_V2, ConfigDict
from githubkit.versions.latest.models import WebhookIssueCommentDeleted

from ._base import Event
from ..message import Message


class IssueCommentDeleted(Event):

    payload: WebhookIssueCommentDeleted

    @cached_property
    def _message(self):
        return Message(self.payload.comment.body)

    @override
    def get_message(self):
        return self._message

    if PYDANTIC_V2:
        model_config = ConfigDict(ignored_types=(cached_property,))
    else:

        class Config:
            keep_untouched = (cached_property,)
