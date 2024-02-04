from githubkit.versions.latest.models import WebhookProjectsV2ProjectCreated

from ._base import Event


class ProjectsV2ProjectCreated(Event):

    payload: WebhookProjectsV2ProjectCreated
