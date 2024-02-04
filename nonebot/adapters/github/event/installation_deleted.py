from githubkit.versions.latest.models import WebhookInstallationDeleted

from ._base import Event


class InstallationDeleted(Event):

    payload: WebhookInstallationDeleted
