from githubkit.versions.latest.models import WebhookProjectColumnDeleted

from ._base import Event


class ProjectColumnDeleted(Event):

    payload: WebhookProjectColumnDeleted
