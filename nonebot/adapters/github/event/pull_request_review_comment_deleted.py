from functools import cached_property
from typing_extensions import override

from githubkit.versions.latest.models import WebhookPullRequestReviewCommentDeleted

from nonebot.compat import PYDANTIC_V2, ConfigDict

from ..message import Message
from ._base import Event


class PullRequestReviewCommentDeleted(Event):
    payload: WebhookPullRequestReviewCommentDeleted

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
