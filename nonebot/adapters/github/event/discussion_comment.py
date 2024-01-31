from githubkit.versions.latest.models import (
    WebhookDiscussionCommentEdited,
    WebhookDiscussionCommentCreated,
    WebhookDiscussionCommentDeleted,
)

from ._base import Event


class DiscussionCommentCreated(Event):

    payload: WebhookDiscussionCommentCreated


class DiscussionCommentDeleted(Event):

    payload: WebhookDiscussionCommentDeleted


class DiscussionCommentEdited(Event):

    payload: WebhookDiscussionCommentEdited
