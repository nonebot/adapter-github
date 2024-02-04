from githubkit.versions.latest.models import WebhookPullRequestReviewThreadResolved

from ._base import Event


class PullRequestReviewThreadResolved(Event):

    payload: WebhookPullRequestReviewThreadResolved
