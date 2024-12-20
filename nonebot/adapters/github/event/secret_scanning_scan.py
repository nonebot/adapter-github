from githubkit.versions.latest.models import WebhookSecretScanningScanCompleted

from ._base import Event


class SecretScanningScanCompleted(Event):
    payload: WebhookSecretScanningScanCompleted
