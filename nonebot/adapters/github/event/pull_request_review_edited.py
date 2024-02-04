from githubkit.versions.latest.models import WebhookPullRequestReviewEdited

from ._base import Event


class PullRequestReviewEdited(Event):

    payload: WebhookPullRequestReviewEdited
