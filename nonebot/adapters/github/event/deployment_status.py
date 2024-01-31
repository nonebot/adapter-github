from githubkit.versions.latest.models import WebhookDeploymentStatusCreated

from ._base import Event


class DeploymentStatusCreated(Event):

    payload: WebhookDeploymentStatusCreated
