from githubkit.versions.latest.models import WebhookProjectCreated

from ._base import Event


class ProjectCreated(Event):

    payload: WebhookProjectCreated
