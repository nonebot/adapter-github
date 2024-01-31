from githubkit.versions.latest.models import (
    WebhookProjectsV2ProjectClosed,
    WebhookProjectsV2ProjectEdited,
    WebhookProjectsV2ProjectCreated,
    WebhookProjectsV2ProjectDeleted,
    WebhookProjectsV2ProjectReopened,
)

from ._base import Event


class ProjectsV2ProjectClosed(Event):

    payload: WebhookProjectsV2ProjectClosed


class ProjectsV2ProjectCreated(Event):

    payload: WebhookProjectsV2ProjectCreated


class ProjectsV2ProjectDeleted(Event):

    payload: WebhookProjectsV2ProjectDeleted


class ProjectsV2ProjectEdited(Event):

    payload: WebhookProjectsV2ProjectEdited


class ProjectsV2ProjectReopened(Event):

    payload: WebhookProjectsV2ProjectReopened
