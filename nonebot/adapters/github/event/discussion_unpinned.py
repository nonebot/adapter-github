from githubkit.versions.latest.models import WebhookDiscussionUnpinned

from ._base import Event


class DiscussionUnpinned(Event):

    payload: WebhookDiscussionUnpinned
