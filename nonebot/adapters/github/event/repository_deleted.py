from githubkit.versions.latest.models import WebhookRepositoryDeleted

from ._base import Event


class RepositoryDeleted(Event):

    payload: WebhookRepositoryDeleted
