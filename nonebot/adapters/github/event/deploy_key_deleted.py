from githubkit.versions.latest.models import WebhookDeployKeyDeleted

from ._base import Event


class DeployKeyDeleted(Event):

    payload: WebhookDeployKeyDeleted
