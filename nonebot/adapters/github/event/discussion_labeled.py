from githubkit.versions.latest.models import WebhookDiscussionLabeled

from ._base import Event


class DiscussionLabeled(Event):

    payload: WebhookDiscussionLabeled
