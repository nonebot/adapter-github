from githubkit.versions.latest.models import WebhookProjectClosed

from ._base import Event


class ProjectClosed(Event):

    payload: WebhookProjectClosed
