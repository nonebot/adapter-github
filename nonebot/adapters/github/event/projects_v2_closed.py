from githubkit.versions.latest.models import WebhookProjectsV2ProjectClosed

from ._base import Event


class ProjectsV2ProjectClosed(Event):

    payload: WebhookProjectsV2ProjectClosed
