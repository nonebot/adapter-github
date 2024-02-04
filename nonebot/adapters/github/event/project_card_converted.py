from githubkit.versions.latest.models import WebhookProjectCardConverted

from ._base import Event


class ProjectCardConverted(Event):

    payload: WebhookProjectCardConverted
