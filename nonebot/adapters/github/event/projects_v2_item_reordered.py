from githubkit.versions.latest.models import WebhookProjectsV2ItemReordered

from ._base import Event


class ProjectsV2ItemReordered(Event):

    payload: WebhookProjectsV2ItemReordered
