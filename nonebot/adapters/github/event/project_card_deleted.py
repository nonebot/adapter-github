from githubkit.versions.latest.models import WebhookProjectCardDeleted

from ._base import Event


class ProjectCardDeleted(Event):

    payload: WebhookProjectCardDeleted
