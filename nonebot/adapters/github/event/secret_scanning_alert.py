from githubkit.versions.latest.models import (
    WebhookSecretScanningAlertCreated,
    WebhookSecretScanningAlertRevoked,
    WebhookSecretScanningAlertReopened,
    WebhookSecretScanningAlertResolved,
)

from ._base import Event


class SecretScanningAlertCreated(Event):

    payload: WebhookSecretScanningAlertCreated


class SecretScanningAlertReopened(Event):

    payload: WebhookSecretScanningAlertReopened


class SecretScanningAlertResolved(Event):

    payload: WebhookSecretScanningAlertResolved


class SecretScanningAlertRevoked(Event):

    payload: WebhookSecretScanningAlertRevoked
