from functools import cached_property
from typing_extensions import override

from githubkit.versions.latest.models import WebhookIssueCommentCreated

from ._base import Event
from ..message import Message


class IssueCommentCreated(Event):

    payload: WebhookIssueCommentCreated

    @override
    def get_type(self) -> str:
        return "message"

    @cached_property
    def _message(self):
        return Message(self.payload.comment.body)

    @override
    def get_message(self):
        return self._message

    class Config:
        keep_untouched = (cached_property,)
