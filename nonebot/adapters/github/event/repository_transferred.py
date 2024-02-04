from githubkit.versions.latest.models import WebhookRepositoryTransferred

from ._base import Event


class RepositoryTransferred(Event):

    payload: WebhookRepositoryTransferred
