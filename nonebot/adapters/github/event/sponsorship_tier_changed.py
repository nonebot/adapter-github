from githubkit.versions.latest.models import WebhookSponsorshipTierChanged

from ._base import Event


class SponsorshipTierChanged(Event):

    payload: WebhookSponsorshipTierChanged
