from githubkit.versions.latest.models import WebhookPullRequestReviewSubmitted

from ._base import Event


class PullRequestReviewSubmitted(Event):

    payload: WebhookPullRequestReviewSubmitted
