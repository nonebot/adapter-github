from githubkit.versions.latest.models import WebhookSponsorshipPendingCancellation

from ._base import Event


class SponsorshipPendingCancellation(Event):

    payload: WebhookSponsorshipPendingCancellation
