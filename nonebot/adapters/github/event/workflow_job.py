from githubkit.versions.latest.models import (
    WebhookWorkflowJobQueued,
    WebhookWorkflowJobWaiting,
    WebhookWorkflowJobCompleted,
    WebhookWorkflowJobInProgress,
)

from ._base import Event


class WorkflowJobCompleted(Event):

    payload: WebhookWorkflowJobCompleted


class WorkflowJobInProgress(Event):

    payload: WebhookWorkflowJobInProgress


class WorkflowJobQueued(Event):

    payload: WebhookWorkflowJobQueued


class WorkflowJobWaiting(Event):

    payload: WebhookWorkflowJobWaiting
