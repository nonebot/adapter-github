from githubkit.versions.latest.models import (
    WebhookInstallationCreated,
    WebhookInstallationDeleted,
    WebhookInstallationSuspend,
    WebhookInstallationUnsuspend,
    WebhookInstallationNewPermissionsAccepted,
)

from ._base import Event


class InstallationCreated(Event):

    payload: WebhookInstallationCreated


class InstallationDeleted(Event):

    payload: WebhookInstallationDeleted


class InstallationNewPermissionsAccepted(Event):

    payload: WebhookInstallationNewPermissionsAccepted


class InstallationSuspend(Event):

    payload: WebhookInstallationSuspend


class InstallationUnsuspend(Event):

    payload: WebhookInstallationUnsuspend
