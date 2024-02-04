from githubkit.versions.latest.models import WebhookDiscussionUnlocked

from ._base import Event


class DiscussionUnlocked(Event):

    payload: WebhookDiscussionUnlocked
