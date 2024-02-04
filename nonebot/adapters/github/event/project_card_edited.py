from githubkit.versions.latest.models import WebhookProjectCardEdited

from ._base import Event


class ProjectCardEdited(Event):

    payload: WebhookProjectCardEdited
