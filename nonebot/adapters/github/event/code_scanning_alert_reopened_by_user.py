from githubkit.versions.latest.models import WebhookCodeScanningAlertReopenedByUser

from ._base import Event


class CodeScanningAlertReopenedByUser(Event):

    payload: WebhookCodeScanningAlertReopenedByUser
