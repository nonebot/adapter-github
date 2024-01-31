from githubkit.versions.latest.models import (
    WebhookDiscussionClosed,
    WebhookDiscussionEdited,
    WebhookDiscussionLocked,
    WebhookDiscussionPinned,
    WebhookDiscussionCreated,
    WebhookDiscussionDeleted,
    WebhookDiscussionLabeled,
    WebhookDiscussionAnswered,
    WebhookDiscussionReopened,
    WebhookDiscussionUnlocked,
    WebhookDiscussionUnpinned,
    WebhookDiscussionUnlabeled,
    WebhookDiscussionUnanswered,
    WebhookDiscussionTransferred,
    WebhookDiscussionCategoryChanged,
)

from ._base import Event


class DiscussionAnswered(Event):

    payload: WebhookDiscussionAnswered


class DiscussionCategoryChanged(Event):

    payload: WebhookDiscussionCategoryChanged


class DiscussionClosed(Event):

    payload: WebhookDiscussionClosed


class DiscussionCreated(Event):

    payload: WebhookDiscussionCreated


class DiscussionDeleted(Event):

    payload: WebhookDiscussionDeleted


class DiscussionEdited(Event):

    payload: WebhookDiscussionEdited


class DiscussionLabeled(Event):

    payload: WebhookDiscussionLabeled


class DiscussionLocked(Event):

    payload: WebhookDiscussionLocked


class DiscussionPinned(Event):

    payload: WebhookDiscussionPinned


class DiscussionReopened(Event):

    payload: WebhookDiscussionReopened


class DiscussionTransferred(Event):

    payload: WebhookDiscussionTransferred


class DiscussionUnanswered(Event):

    payload: WebhookDiscussionUnanswered


class DiscussionUnlabeled(Event):

    payload: WebhookDiscussionUnlabeled


class DiscussionUnlocked(Event):

    payload: WebhookDiscussionUnlocked


class DiscussionUnpinned(Event):

    payload: WebhookDiscussionUnpinned
