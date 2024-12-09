from githubkit.versions.latest.models import WebhookSecretScanningAlertPubliclyLeaked

from ._base import Event


class SecretScanningAlertPubliclyLeaked(Event):
    payload: WebhookSecretScanningAlertPubliclyLeaked
