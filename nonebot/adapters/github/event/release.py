from githubkit.versions.latest.models import (
    WebhookReleaseEdited,
    WebhookReleaseCreated,
    WebhookReleaseDeleted,
    WebhookReleaseReleased,
    WebhookReleasePublished,
    WebhookReleasePrereleased,
    WebhookReleaseUnpublished,
)

from ._base import Event


class ReleaseCreated(Event):

    payload: WebhookReleaseCreated


class ReleaseDeleted(Event):

    payload: WebhookReleaseDeleted


class ReleaseEdited(Event):

    payload: WebhookReleaseEdited


class ReleasePrereleased(Event):

    payload: WebhookReleasePrereleased


class ReleasePublished(Event):

    payload: WebhookReleasePublished


class ReleaseReleased(Event):

    payload: WebhookReleaseReleased


class ReleaseUnpublished(Event):

    payload: WebhookReleaseUnpublished
