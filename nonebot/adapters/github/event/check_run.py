from githubkit.versions.latest.models import (
    WebhookCheckRunCreated,
    WebhookCheckRunCompleted,
    WebhookCheckRunRerequested,
    WebhookCheckRunRequestedAction,
)

from ._base import Event


class CheckRunCompleted(Event):

    payload: WebhookCheckRunCompleted


class CheckRunCreated(Event):

    payload: WebhookCheckRunCreated


class CheckRunRequestedAction(Event):

    payload: WebhookCheckRunRequestedAction


class CheckRunRerequested(Event):

    payload: WebhookCheckRunRerequested
