from githubkit.versions.latest.models import WebhookProjectReopened

from ._base import Event


class ProjectReopened(Event):

    payload: WebhookProjectReopened
