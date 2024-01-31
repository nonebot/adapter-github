from githubkit.versions.latest.models import WebhookDeploymentCreated

from ._base import Event


class DeploymentCreated(Event):

    payload: WebhookDeploymentCreated
