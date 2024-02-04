from githubkit.versions.latest.models import WebhookPullRequestReviewThreadUnresolved

from ._base import Event


class PullRequestReviewThreadUnresolved(Event):

    payload: WebhookPullRequestReviewThreadUnresolved
