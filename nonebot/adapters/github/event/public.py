from githubkit.versions.latest.models import WebhookPublic

from ._base import Event


class Public(Event):

    payload: WebhookPublic
