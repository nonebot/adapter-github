from githubkit.versions.latest.models import WebhookInstallationTargetRenamed

from ._base import Event


class InstallationTargetRenamed(Event):

    payload: WebhookInstallationTargetRenamed
