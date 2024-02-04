from githubkit.versions.latest.models import WebhookSponsorshipEdited

from ._base import Event


class SponsorshipEdited(Event):

    payload: WebhookSponsorshipEdited
