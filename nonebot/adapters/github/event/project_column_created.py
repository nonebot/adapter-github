from githubkit.versions.latest.models import WebhookProjectColumnCreated

from ._base import Event


class ProjectColumnCreated(Event):

    payload: WebhookProjectColumnCreated
