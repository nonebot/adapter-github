from githubkit.versions.latest.models import WebhookProjectsV2ItemArchived

from ._base import Event


class ProjectsV2ItemArchived(Event):

    payload: WebhookProjectsV2ItemArchived
