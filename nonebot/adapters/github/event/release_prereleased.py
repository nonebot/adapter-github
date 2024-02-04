from githubkit.versions.latest.models import WebhookReleasePrereleased

from ._base import Event


class ReleasePrereleased(Event):

    payload: WebhookReleasePrereleased
