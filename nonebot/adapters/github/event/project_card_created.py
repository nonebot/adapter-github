from githubkit.versions.latest.models import WebhookProjectCardCreated

from ._base import Event


class ProjectCardCreated(Event):

    payload: WebhookProjectCardCreated
