from githubkit.versions.latest.models import WebhookProjectColumnMoved

from ._base import Event


class ProjectColumnMoved(Event):

    payload: WebhookProjectColumnMoved
