from githubkit.versions.latest.models import WebhookWorkflowJobWaiting

from ._base import Event


class WorkflowJobWaiting(Event):

    payload: WebhookWorkflowJobWaiting
