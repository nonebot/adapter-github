from githubkit.versions.latest.models import WebhookProjectsV2StatusUpdateDeleted

from ._base import Event


class ProjectsV2StatusUpdateDeleted(Event):
    payload: WebhookProjectsV2StatusUpdateDeleted
