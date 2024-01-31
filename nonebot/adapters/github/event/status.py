from githubkit.versions.latest.models import WebhookStatus

from ._base import Event


class Status(Event):

    payload: WebhookStatus
