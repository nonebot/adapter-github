from githubkit.versions.latest.models import WebhookSponsorshipCreated

from ._base import Event


class SponsorshipCreated(Event):

    payload: WebhookSponsorshipCreated
