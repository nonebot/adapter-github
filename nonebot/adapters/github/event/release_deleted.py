from githubkit.versions.latest.models import WebhookReleaseDeleted

from ._base import Event


class ReleaseDeleted(Event):

    payload: WebhookReleaseDeleted
