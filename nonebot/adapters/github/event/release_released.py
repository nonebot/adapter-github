from githubkit.versions.latest.models import WebhookReleaseReleased

from ._base import Event


class ReleaseReleased(Event):

    payload: WebhookReleaseReleased
