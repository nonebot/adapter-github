from githubkit.versions.latest.models import (
    WebhookCodeScanningAlertFixed,
    WebhookCodeScanningAlertCreated,
    WebhookCodeScanningAlertReopened,
    WebhookCodeScanningAlertClosedByUser,
    WebhookCodeScanningAlertReopenedByUser,
    WebhookCodeScanningAlertAppearedInBranch,
)

from ._base import Event


class CodeScanningAlertAppearedInBranch(Event):

    payload: WebhookCodeScanningAlertAppearedInBranch


class CodeScanningAlertClosedByUser(Event):

    payload: WebhookCodeScanningAlertClosedByUser


class CodeScanningAlertCreated(Event):

    payload: WebhookCodeScanningAlertCreated


class CodeScanningAlertFixed(Event):

    payload: WebhookCodeScanningAlertFixed


class CodeScanningAlertReopened(Event):

    payload: WebhookCodeScanningAlertReopened


class CodeScanningAlertReopenedByUser(Event):

    payload: WebhookCodeScanningAlertReopenedByUser
