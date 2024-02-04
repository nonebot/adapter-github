from githubkit.versions.latest.models import WebhookStarDeleted

from ._base import Event


class StarDeleted(Event):

    payload: WebhookStarDeleted
