from githubkit.versions.latest.models import (
    WebhookProjectCardMoved,
    WebhookProjectCardEdited,
    WebhookProjectCardCreated,
    WebhookProjectCardDeleted,
    WebhookProjectCardConverted,
)

from ._base import Event


class ProjectCardConverted(Event):

    payload: WebhookProjectCardConverted


class ProjectCardCreated(Event):

    payload: WebhookProjectCardCreated


class ProjectCardDeleted(Event):

    payload: WebhookProjectCardDeleted


class ProjectCardEdited(Event):

    payload: WebhookProjectCardEdited


class ProjectCardMoved(Event):

    payload: WebhookProjectCardMoved
