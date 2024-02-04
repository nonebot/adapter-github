from githubkit.versions.latest.models import WebhookCodeScanningAlertCreated

from ._base import Event


class CodeScanningAlertCreated(Event):

    payload: WebhookCodeScanningAlertCreated
