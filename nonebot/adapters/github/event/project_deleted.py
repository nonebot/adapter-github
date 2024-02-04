from githubkit.versions.latest.models import WebhookProjectDeleted

from ._base import Event


class ProjectDeleted(Event):

    payload: WebhookProjectDeleted
