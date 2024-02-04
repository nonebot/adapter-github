from githubkit.versions.latest.models import WebhookMilestoneClosed

from ._base import Event


class MilestoneClosed(Event):

    payload: WebhookMilestoneClosed
