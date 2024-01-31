from githubkit.versions.latest.models import WebhookPing

from ._base import Event


class Ping(Event):

    payload: WebhookPing
