from githubkit.versions.latest.models import WebhookSecretScanningAlertLocationCreated

from ._base import Event


class SecretScanningAlertLocationCreated(Event):

    payload: WebhookSecretScanningAlertLocationCreated
