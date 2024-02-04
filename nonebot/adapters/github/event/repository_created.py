from githubkit.versions.latest.models import WebhookRepositoryCreated

from ._base import Event


class RepositoryCreated(Event):

    payload: WebhookRepositoryCreated
