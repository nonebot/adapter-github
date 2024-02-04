from githubkit.versions.latest.models import WebhookDiscussionClosed

from ._base import Event


class DiscussionClosed(Event):

    payload: WebhookDiscussionClosed
