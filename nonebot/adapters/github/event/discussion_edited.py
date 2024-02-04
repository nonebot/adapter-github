from githubkit.versions.latest.models import WebhookDiscussionEdited

from ._base import Event


class DiscussionEdited(Event):

    payload: WebhookDiscussionEdited
