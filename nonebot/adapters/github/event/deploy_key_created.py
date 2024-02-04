from githubkit.versions.latest.models import WebhookDeployKeyCreated

from ._base import Event


class DeployKeyCreated(Event):

    payload: WebhookDeployKeyCreated
