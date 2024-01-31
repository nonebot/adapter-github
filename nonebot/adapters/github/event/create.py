from githubkit.versions.latest.models import WebhookCreate

from ._base import Event


class Create(Event):

    payload: WebhookCreate
