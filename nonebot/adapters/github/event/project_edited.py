from githubkit.versions.latest.models import WebhookProjectEdited

from ._base import Event


class ProjectEdited(Event):

    payload: WebhookProjectEdited
