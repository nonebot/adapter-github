from githubkit.versions.latest.models import (
    WebhookDeployKeyCreated,
    WebhookDeployKeyDeleted,
)

from ._base import Event


class DeployKeyCreated(Event):

    payload: WebhookDeployKeyCreated


class DeployKeyDeleted(Event):

    payload: WebhookDeployKeyDeleted
