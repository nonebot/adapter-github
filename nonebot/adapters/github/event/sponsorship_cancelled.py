from githubkit.versions.latest.models import WebhookSponsorshipCancelled

from ._base import Event


class SponsorshipCancelled(Event):

    payload: WebhookSponsorshipCancelled
