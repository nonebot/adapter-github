from githubkit.versions.latest.models import WebhookSecretScanningAlertResolved

from ._base import Event


class SecretScanningAlertResolved(Event):

    payload: WebhookSecretScanningAlertResolved
