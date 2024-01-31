from typing import Union

from githubkit.versions.latest.models import (
    WebhookPullRequestClosed,
    WebhookPullRequestEdited,
    WebhookPullRequestLocked,
    WebhookPullRequestOpened,
    WebhookPullRequestLabeled,
    WebhookPullRequestAssigned,
    WebhookPullRequestDequeued,
    WebhookPullRequestEnqueued,
    WebhookPullRequestReopened,
    WebhookPullRequestUnlocked,
    WebhookPullRequestUnlabeled,
    WebhookPullRequestMilestoned,
    WebhookPullRequestUnassigned,
    WebhookPullRequestSynchronize,
    WebhookPullRequestDemilestoned,
    WebhookPullRequestReadyForReview,
    WebhookPullRequestAutoMergeEnabled,
    WebhookPullRequestConvertedToDraft,
    WebhookPullRequestAutoMergeDisabled,
    WebhookPullRequestReviewRequestedOneof0,
    WebhookPullRequestReviewRequestedOneof1,
    WebhookPullRequestReviewRequestRemovedOneof0,
    WebhookPullRequestReviewRequestRemovedOneof1,
)

from ._base import Event


class PullRequestAssigned(Event):

    payload: WebhookPullRequestAssigned


class PullRequestAutoMergeDisabled(Event):

    payload: WebhookPullRequestAutoMergeDisabled


class PullRequestAutoMergeEnabled(Event):

    payload: WebhookPullRequestAutoMergeEnabled


class PullRequestClosed(Event):

    payload: WebhookPullRequestClosed


class PullRequestConvertedToDraft(Event):

    payload: WebhookPullRequestConvertedToDraft


class PullRequestDemilestoned(Event):

    payload: WebhookPullRequestDemilestoned


class PullRequestDequeued(Event):

    payload: WebhookPullRequestDequeued


class PullRequestEdited(Event):

    payload: WebhookPullRequestEdited


class PullRequestEnqueued(Event):

    payload: WebhookPullRequestEnqueued


class PullRequestLabeled(Event):

    payload: WebhookPullRequestLabeled


class PullRequestLocked(Event):

    payload: WebhookPullRequestLocked


class PullRequestMilestoned(Event):

    payload: WebhookPullRequestMilestoned


class PullRequestOpened(Event):

    payload: WebhookPullRequestOpened


class PullRequestReadyForReview(Event):

    payload: WebhookPullRequestReadyForReview


class PullRequestReopened(Event):

    payload: WebhookPullRequestReopened


class PullRequestReviewRequestRemoved(Event):

    payload: Union[
        WebhookPullRequestReviewRequestRemovedOneof0,
        WebhookPullRequestReviewRequestRemovedOneof1,
    ]


class PullRequestReviewRequested(Event):

    payload: Union[
        WebhookPullRequestReviewRequestedOneof0, WebhookPullRequestReviewRequestedOneof1
    ]


class PullRequestSynchronize(Event):

    payload: WebhookPullRequestSynchronize


class PullRequestUnassigned(Event):

    payload: WebhookPullRequestUnassigned


class PullRequestUnlabeled(Event):

    payload: WebhookPullRequestUnlabeled


class PullRequestUnlocked(Event):

    payload: WebhookPullRequestUnlocked
