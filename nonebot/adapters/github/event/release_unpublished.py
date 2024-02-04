from githubkit.versions.latest.models import WebhookReleaseUnpublished

from ._base import Event


class ReleaseUnpublished(Event):

    payload: WebhookReleaseUnpublished
