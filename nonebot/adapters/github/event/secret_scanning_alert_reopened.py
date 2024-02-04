from githubkit.versions.latest.models import WebhookSecretScanningAlertReopened

from ._base import Event


class SecretScanningAlertReopened(Event):

    payload: WebhookSecretScanningAlertReopened
