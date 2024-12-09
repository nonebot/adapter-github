from githubkit.versions.latest.models import WebhookProjectsV2StatusUpdateCreated

from ._base import Event


class ProjectsV2StatusUpdateCreated(Event):
    payload: WebhookProjectsV2StatusUpdateCreated
