from githubkit.versions.latest.models import WebhookPush

from ._base import Event


class Push(Event):

    payload: WebhookPush
