from githubkit.versions.latest.models import (
    WebhookProjectColumnMoved,
    WebhookProjectColumnEdited,
    WebhookProjectColumnCreated,
    WebhookProjectColumnDeleted,
)

from ._base import Event


class ProjectColumnCreated(Event):

    payload: WebhookProjectColumnCreated


class ProjectColumnDeleted(Event):

    payload: WebhookProjectColumnDeleted


class ProjectColumnEdited(Event):

    payload: WebhookProjectColumnEdited


class ProjectColumnMoved(Event):

    payload: WebhookProjectColumnMoved
