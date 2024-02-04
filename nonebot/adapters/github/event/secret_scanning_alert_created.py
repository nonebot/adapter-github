from githubkit.versions.latest.models import WebhookSecretScanningAlertCreated

from ._base import Event


class SecretScanningAlertCreated(Event):

    payload: WebhookSecretScanningAlertCreated
