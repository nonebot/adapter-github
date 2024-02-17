from githubkit.versions.latest.models import WebhookSecretScanningAlertValidated

from ._base import Event


class SecretScanningAlertValidated(Event):

    payload: WebhookSecretScanningAlertValidated
