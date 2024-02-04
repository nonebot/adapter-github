from githubkit.versions.latest.models import WebhookDiscussionCommentEdited

from ._base import Event


class DiscussionCommentEdited(Event):

    payload: WebhookDiscussionCommentEdited
