from githubkit.versions.latest.models import WebhookStarCreated, WebhookStarDeleted

from ._base import Event


class StarCreated(Event):

    payload: WebhookStarCreated


class StarDeleted(Event):

    payload: WebhookStarDeleted
