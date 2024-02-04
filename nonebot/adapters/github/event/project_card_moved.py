from githubkit.versions.latest.models import WebhookProjectCardMoved

from ._base import Event


class ProjectCardMoved(Event):

    payload: WebhookProjectCardMoved
