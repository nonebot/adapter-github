from githubkit.versions.latest.models import WebhookProjectsV2ProjectEdited

from ._base import Event


class ProjectsV2ProjectEdited(Event):

    payload: WebhookProjectsV2ProjectEdited
