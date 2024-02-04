from githubkit.versions.latest.models import WebhookWorkflowRunRequested

from ._base import Event


class WorkflowRunRequested(Event):

    payload: WebhookWorkflowRunRequested
