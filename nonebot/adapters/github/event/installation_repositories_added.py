from githubkit.versions.latest.models import WebhookInstallationRepositoriesAdded

from ._base import Event


class InstallationRepositoriesAdded(Event):

    payload: WebhookInstallationRepositoriesAdded
