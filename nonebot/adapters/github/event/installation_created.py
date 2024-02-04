from githubkit.versions.latest.models import WebhookInstallationCreated

from ._base import Event


class InstallationCreated(Event):

    payload: WebhookInstallationCreated
