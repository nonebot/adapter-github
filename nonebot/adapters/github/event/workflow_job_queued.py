from githubkit.versions.latest.models import WebhookWorkflowJobQueued

from ._base import Event


class WorkflowJobQueued(Event):

    payload: WebhookWorkflowJobQueued
