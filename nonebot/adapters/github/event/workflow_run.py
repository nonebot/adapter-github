from githubkit.versions.latest.models import (
    WebhookWorkflowRunCompleted,
    WebhookWorkflowRunRequested,
    WebhookWorkflowRunInProgress,
)

from ._base import Event


class WorkflowRunCompleted(Event):

    payload: WebhookWorkflowRunCompleted


class WorkflowRunInProgress(Event):

    payload: WebhookWorkflowRunInProgress


class WorkflowRunRequested(Event):

    payload: WebhookWorkflowRunRequested
