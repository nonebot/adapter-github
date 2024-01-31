from githubkit.versions.latest.models import (
    WebhookDeploymentReviewApproved,
    WebhookDeploymentReviewRejected,
    WebhookDeploymentReviewRequested,
)

from ._base import Event


class DeploymentReviewApproved(Event):

    payload: WebhookDeploymentReviewApproved


class DeploymentReviewRejected(Event):

    payload: WebhookDeploymentReviewRejected


class DeploymentReviewRequested(Event):

    payload: WebhookDeploymentReviewRequested
