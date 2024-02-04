from githubkit.versions.latest.models import WebhookDiscussionCommentDeleted

from ._base import Event


class DiscussionCommentDeleted(Event):

    payload: WebhookDiscussionCommentDeleted
