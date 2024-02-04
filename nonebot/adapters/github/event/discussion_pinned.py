from githubkit.versions.latest.models import WebhookDiscussionPinned

from ._base import Event


class DiscussionPinned(Event):

    payload: WebhookDiscussionPinned
