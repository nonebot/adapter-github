from githubkit.versions.latest.models import WebhookDiscussionCommentCreated

from ._base import Event


class DiscussionCommentCreated(Event):

    payload: WebhookDiscussionCommentCreated
