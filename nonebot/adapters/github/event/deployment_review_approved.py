from githubkit.versions.latest.models import WebhookDeploymentReviewApproved

from ._base import Event


class DeploymentReviewApproved(Event):

    payload: WebhookDeploymentReviewApproved
