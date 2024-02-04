from githubkit.versions.latest.models import WebhookProjectsV2ItemEdited

from ._base import Event


class ProjectsV2ItemEdited(Event):

    payload: WebhookProjectsV2ItemEdited
