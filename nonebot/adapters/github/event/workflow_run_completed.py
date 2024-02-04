from githubkit.versions.latest.models import WebhookWorkflowRunCompleted

from ._base import Event


class WorkflowRunCompleted(Event):

    payload: WebhookWorkflowRunCompleted
