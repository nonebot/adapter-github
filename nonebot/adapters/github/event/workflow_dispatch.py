from githubkit.versions.latest.models import WebhookWorkflowDispatch

from ._base import Event


class WorkflowDispatch(Event):

    payload: WebhookWorkflowDispatch
