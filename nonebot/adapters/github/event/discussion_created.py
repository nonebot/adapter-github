from githubkit.versions.latest.models import WebhookDiscussionCreated

from ._base import Event


class DiscussionCreated(Event):

    payload: WebhookDiscussionCreated
