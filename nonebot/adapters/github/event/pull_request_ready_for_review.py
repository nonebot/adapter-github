from githubkit.versions.latest.models import WebhookPullRequestReadyForReview

from ._base import Event


class PullRequestReadyForReview(Event):

    payload: WebhookPullRequestReadyForReview
