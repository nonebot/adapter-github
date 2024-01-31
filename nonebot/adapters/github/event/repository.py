from githubkit.versions.latest.models import (
    WebhookRepositoryEdited,
    WebhookRepositoryCreated,
    WebhookRepositoryDeleted,
    WebhookRepositoryRenamed,
    WebhookRepositoryArchived,
    WebhookRepositoryPrivatized,
    WebhookRepositoryPublicized,
    WebhookRepositoryUnarchived,
    WebhookRepositoryTransferred,
)

from ._base import Event


class RepositoryArchived(Event):

    payload: WebhookRepositoryArchived


class RepositoryCreated(Event):

    payload: WebhookRepositoryCreated


class RepositoryDeleted(Event):

    payload: WebhookRepositoryDeleted


class RepositoryEdited(Event):

    payload: WebhookRepositoryEdited


class RepositoryPrivatized(Event):

    payload: WebhookRepositoryPrivatized


class RepositoryPublicized(Event):

    payload: WebhookRepositoryPublicized


class RepositoryRenamed(Event):

    payload: WebhookRepositoryRenamed


class RepositoryTransferred(Event):

    payload: WebhookRepositoryTransferred


class RepositoryUnarchived(Event):

    payload: WebhookRepositoryUnarchived
