from githubkit.versions.latest.models import WebhookSecretScanningAlertRevoked

from ._base import Event


class SecretScanningAlertRevoked(Event):

    payload: WebhookSecretScanningAlertRevoked
