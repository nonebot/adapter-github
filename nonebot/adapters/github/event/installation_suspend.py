from githubkit.versions.latest.models import WebhookInstallationSuspend

from ._base import Event


class InstallationSuspend(Event):

    payload: WebhookInstallationSuspend
