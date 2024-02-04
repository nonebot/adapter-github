from githubkit.versions.latest.models import WebhookInstallationUnsuspend

from ._base import Event


class InstallationUnsuspend(Event):

    payload: WebhookInstallationUnsuspend
