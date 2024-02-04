from githubkit.versions.latest.models import WebhookStarCreated

from ._base import Event


class StarCreated(Event):

    payload: WebhookStarCreated
