from githubkit.versions.latest.models import (
    WebhookPullRequestReviewThreadResolved,
    WebhookPullRequestReviewThreadUnresolved,
)

from ._base import Event


class PullRequestReviewThreadResolved(Event):

    payload: WebhookPullRequestReviewThreadResolved


class PullRequestReviewThreadUnresolved(Event):

    payload: WebhookPullRequestReviewThreadUnresolved
