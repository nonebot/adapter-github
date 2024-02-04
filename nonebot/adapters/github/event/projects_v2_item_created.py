from githubkit.versions.latest.models import WebhookProjectsV2ItemCreated

from ._base import Event


class ProjectsV2ItemCreated(Event):

    payload: WebhookProjectsV2ItemCreated
