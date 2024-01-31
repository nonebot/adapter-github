from githubkit.versions.latest.models import (
    WebhookProjectsV2ItemEdited,
    WebhookProjectsV2ItemCreated,
    WebhookProjectsV2ItemDeleted,
    WebhookProjectsV2ItemArchived,
    WebhookProjectsV2ItemRestored,
    WebhookProjectsV2ItemConverted,
    WebhookProjectsV2ItemReordered,
)

from ._base import Event


class ProjectsV2ItemArchived(Event):

    payload: WebhookProjectsV2ItemArchived


class ProjectsV2ItemConverted(Event):

    payload: WebhookProjectsV2ItemConverted


class ProjectsV2ItemCreated(Event):

    payload: WebhookProjectsV2ItemCreated


class ProjectsV2ItemDeleted(Event):

    payload: WebhookProjectsV2ItemDeleted


class ProjectsV2ItemEdited(Event):

    payload: WebhookProjectsV2ItemEdited


class ProjectsV2ItemReordered(Event):

    payload: WebhookProjectsV2ItemReordered


class ProjectsV2ItemRestored(Event):

    payload: WebhookProjectsV2ItemRestored
