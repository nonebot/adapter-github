from githubkit.versions.latest.models import (
    WebhookSponsorshipEdited,
    WebhookSponsorshipCreated,
    WebhookSponsorshipCancelled,
    WebhookSponsorshipTierChanged,
    WebhookSponsorshipPendingTierChange,
    WebhookSponsorshipPendingCancellation,
)

from ._base import Event


class SponsorshipCancelled(Event):

    payload: WebhookSponsorshipCancelled


class SponsorshipCreated(Event):

    payload: WebhookSponsorshipCreated


class SponsorshipEdited(Event):

    payload: WebhookSponsorshipEdited


class SponsorshipPendingCancellation(Event):

    payload: WebhookSponsorshipPendingCancellation


class SponsorshipPendingTierChange(Event):

    payload: WebhookSponsorshipPendingTierChange


class SponsorshipTierChanged(Event):

    payload: WebhookSponsorshipTierChanged
