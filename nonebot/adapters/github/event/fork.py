from githubkit.versions.latest.models import WebhookFork

from ._base import Event


class Fork(Event):

    payload: WebhookFork
