from githubkit.versions.latest.models import WebhookDiscussionDeleted

from ._base import Event


class DiscussionDeleted(Event):

    payload: WebhookDiscussionDeleted
