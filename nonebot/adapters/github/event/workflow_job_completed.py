from githubkit.versions.latest.models import WebhookWorkflowJobCompleted

from ._base import Event


class WorkflowJobCompleted(Event):

    payload: WebhookWorkflowJobCompleted
