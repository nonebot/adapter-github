from githubkit.versions.latest.models import WebhookDeploymentReviewRejected

from ._base import Event


class DeploymentReviewRejected(Event):

    payload: WebhookDeploymentReviewRejected
