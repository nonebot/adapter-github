from githubkit.versions.latest.models import WebhookRepositoryRenamed

from ._base import Event


class RepositoryRenamed(Event):

    payload: WebhookRepositoryRenamed
