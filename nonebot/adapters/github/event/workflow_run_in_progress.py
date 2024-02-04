from githubkit.versions.latest.models import WebhookWorkflowRunInProgress

from ._base import Event


class WorkflowRunInProgress(Event):

    payload: WebhookWorkflowRunInProgress
