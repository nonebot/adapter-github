from githubkit.versions.latest.models import WebhookInstallationRepositoriesRemoved

from ._base import Event


class InstallationRepositoriesRemoved(Event):

    payload: WebhookInstallationRepositoriesRemoved
