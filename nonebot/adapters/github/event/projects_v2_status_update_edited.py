from githubkit.versions.latest.models import WebhookProjectsV2StatusUpdateEdited

from ._base import Event


class ProjectsV2StatusUpdateEdited(Event):
    payload: WebhookProjectsV2StatusUpdateEdited
