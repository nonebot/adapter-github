from githubkit.versions.latest.models import WebhookCodeScanningAlertReopened

from ._base import Event


class CodeScanningAlertReopened(Event):

    payload: WebhookCodeScanningAlertReopened
