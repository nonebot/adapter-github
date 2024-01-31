from githubkit.versions.latest.models import (
    WebhookDependabotAlertFixed,
    WebhookDependabotAlertCreated,
    WebhookDependabotAlertReopened,
    WebhookDependabotAlertDismissed,
    WebhookDependabotAlertAutoReopened,
    WebhookDependabotAlertReintroduced,
    WebhookDependabotAlertAutoDismissed,
)

from ._base import Event


class DependabotAlertAutoDismissed(Event):

    payload: WebhookDependabotAlertAutoDismissed


class DependabotAlertAutoReopened(Event):

    payload: WebhookDependabotAlertAutoReopened


class DependabotAlertCreated(Event):

    payload: WebhookDependabotAlertCreated


class DependabotAlertDismissed(Event):

    payload: WebhookDependabotAlertDismissed


class DependabotAlertFixed(Event):

    payload: WebhookDependabotAlertFixed


class DependabotAlertReintroduced(Event):

    payload: WebhookDependabotAlertReintroduced


class DependabotAlertReopened(Event):

    payload: WebhookDependabotAlertReopened
