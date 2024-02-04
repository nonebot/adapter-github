from githubkit.versions.latest.models import WebhookCodeScanningAlertFixed

from ._base import Event


class CodeScanningAlertFixed(Event):

    payload: WebhookCodeScanningAlertFixed
