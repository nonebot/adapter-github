from githubkit.versions.latest.models import (
    WebhookCheckSuiteCompleted,
    WebhookCheckSuiteRequested,
    WebhookCheckSuiteRerequested,
)

from ._base import Event


class CheckSuiteCompleted(Event):

    payload: WebhookCheckSuiteCompleted


class CheckSuiteRequested(Event):

    payload: WebhookCheckSuiteRequested


class CheckSuiteRerequested(Event):

    payload: WebhookCheckSuiteRerequested
