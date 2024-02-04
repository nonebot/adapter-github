from githubkit.versions.latest.models import WebhookCodeScanningAlertAppearedInBranch

from ._base import Event


class CodeScanningAlertAppearedInBranch(Event):

    payload: WebhookCodeScanningAlertAppearedInBranch
