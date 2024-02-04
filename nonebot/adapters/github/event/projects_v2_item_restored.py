from githubkit.versions.latest.models import WebhookProjectsV2ItemRestored

from ._base import Event


class ProjectsV2ItemRestored(Event):

    payload: WebhookProjectsV2ItemRestored
