from githubkit.versions.latest.models import WebhookDeploymentReviewRequested

from ._base import Event


class DeploymentReviewRequested(Event):

    payload: WebhookDeploymentReviewRequested
