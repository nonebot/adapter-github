from githubkit.versions.latest.models import WebhookProjectsV2ProjectDeleted

from ._base import Event


class ProjectsV2ProjectDeleted(Event):

    payload: WebhookProjectsV2ProjectDeleted
