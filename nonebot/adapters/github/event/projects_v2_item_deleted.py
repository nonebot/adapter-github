from githubkit.versions.latest.models import WebhookProjectsV2ItemDeleted

from ._base import Event


class ProjectsV2ItemDeleted(Event):

    payload: WebhookProjectsV2ItemDeleted
