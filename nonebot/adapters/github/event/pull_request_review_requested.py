from typing import Union

from githubkit.versions.latest.models import (
    WebhookPullRequestReviewRequestedOneof0,
    WebhookPullRequestReviewRequestedOneof1,
)

from ._base import Event


class PullRequestReviewRequested(Event):

    payload: Union[
        WebhookPullRequestReviewRequestedOneof0, WebhookPullRequestReviewRequestedOneof1
    ]
