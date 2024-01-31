from githubkit.versions.latest.models import WebhookDelete

from ._base import Event


class Delete(Event):

    payload: WebhookDelete
