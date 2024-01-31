from githubkit.versions.latest.models import (
    WebhookPullRequestReviewEdited,
    WebhookPullRequestReviewDismissed,
    WebhookPullRequestReviewSubmitted,
)

from ._base import Event


class PullRequestReviewDismissed(Event):

    payload: WebhookPullRequestReviewDismissed


class PullRequestReviewEdited(Event):

    payload: WebhookPullRequestReviewEdited


class PullRequestReviewSubmitted(Event):

    payload: WebhookPullRequestReviewSubmitted
