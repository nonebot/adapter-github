from githubkit.versions.latest.models import WebhookProjectsV2ProjectReopened

from ._base import Event


class ProjectsV2ProjectReopened(Event):

    payload: WebhookProjectsV2ProjectReopened
