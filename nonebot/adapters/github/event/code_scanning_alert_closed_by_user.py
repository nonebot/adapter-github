from githubkit.versions.latest.models import WebhookCodeScanningAlertClosedByUser

from ._base import Event


class CodeScanningAlertClosedByUser(Event):

    payload: WebhookCodeScanningAlertClosedByUser
