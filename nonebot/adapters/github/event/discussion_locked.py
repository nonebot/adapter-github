from githubkit.versions.latest.models import WebhookDiscussionLocked

from ._base import Event


class DiscussionLocked(Event):

    payload: WebhookDiscussionLocked
