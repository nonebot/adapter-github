from githubkit.versions.latest.models import (
    WebhookProjectClosed,
    WebhookProjectEdited,
    WebhookProjectCreated,
    WebhookProjectDeleted,
    WebhookProjectReopened,
)

from ._base import Event


class ProjectClosed(Event):

    payload: WebhookProjectClosed


class ProjectCreated(Event):

    payload: WebhookProjectCreated


class ProjectDeleted(Event):

    payload: WebhookProjectDeleted


class ProjectEdited(Event):

    payload: WebhookProjectEdited


class ProjectReopened(Event):

    payload: WebhookProjectReopened
