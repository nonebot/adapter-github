from githubkit.versions.latest.models import WebhookProjectsV2ItemConverted

from ._base import Event


class ProjectsV2ItemConverted(Event):

    payload: WebhookProjectsV2ItemConverted
