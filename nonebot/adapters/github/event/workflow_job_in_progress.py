from githubkit.versions.latest.models import WebhookWorkflowJobInProgress

from ._base import Event


class WorkflowJobInProgress(Event):

    payload: WebhookWorkflowJobInProgress
