from githubkit.versions.latest.models import WebhookReleasePublished

from ._base import Event


class ReleasePublished(Event):

    payload: WebhookReleasePublished
