from typing import Union

from githubkit.versions.latest.models import (
    WebhookPullRequestReviewRequestRemovedOneof0,
    WebhookPullRequestReviewRequestRemovedOneof1,
)

from ._base import Event


class PullRequestReviewRequestRemoved(Event):

    payload: Union[
        WebhookPullRequestReviewRequestRemovedOneof0,
        WebhookPullRequestReviewRequestRemovedOneof1,
    ]
