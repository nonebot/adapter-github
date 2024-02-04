from githubkit.versions.latest.models import WebhookSponsorshipPendingTierChange

from ._base import Event


class SponsorshipPendingTierChange(Event):

    payload: WebhookSponsorshipPendingTierChange
