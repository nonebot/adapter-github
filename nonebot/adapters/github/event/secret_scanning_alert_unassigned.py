from githubkit.versions.latest.models import WebhookSecretScanningAlertUnassigned

from ._base import Event


class SecretScanningAlertUnassigned(Event):
    payload: WebhookSecretScanningAlertUnassigned
