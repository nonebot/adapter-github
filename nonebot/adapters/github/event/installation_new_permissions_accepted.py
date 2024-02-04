from githubkit.versions.latest.models import WebhookInstallationNewPermissionsAccepted

from ._base import Event


class InstallationNewPermissionsAccepted(Event):

    payload: WebhookInstallationNewPermissionsAccepted
