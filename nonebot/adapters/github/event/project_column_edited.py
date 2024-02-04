from githubkit.versions.latest.models import WebhookProjectColumnEdited

from ._base import Event


class ProjectColumnEdited(Event):

    payload: WebhookProjectColumnEdited
