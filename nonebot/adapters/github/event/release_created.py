from githubkit.versions.latest.models import WebhookReleaseCreated

from ._base import Event


class ReleaseCreated(Event):

    payload: WebhookReleaseCreated
