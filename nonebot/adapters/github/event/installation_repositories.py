from githubkit.versions.latest.models import (
    WebhookInstallationRepositoriesAdded,
    WebhookInstallationRepositoriesRemoved,
)

from ._base import Event


class InstallationRepositoriesAdded(Event):

    payload: WebhookInstallationRepositoriesAdded


class InstallationRepositoriesRemoved(Event):

    payload: WebhookInstallationRepositoriesRemoved
