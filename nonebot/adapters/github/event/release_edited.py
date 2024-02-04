from githubkit.versions.latest.models import WebhookReleaseEdited

from ._base import Event


class ReleaseEdited(Event):

    payload: WebhookReleaseEdited
