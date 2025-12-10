from githubkit.versions.latest.models import WebhookSecretScanningAlertAssigned

from ._base import Event


class SecretScanningAlertAssigned(Event):
    payload: WebhookSecretScanningAlertAssigned
