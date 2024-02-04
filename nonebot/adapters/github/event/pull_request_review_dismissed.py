from githubkit.versions.latest.models import WebhookPullRequestReviewDismissed

from ._base import Event


class PullRequestReviewDismissed(Event):

    payload: WebhookPullRequestReviewDismissed
