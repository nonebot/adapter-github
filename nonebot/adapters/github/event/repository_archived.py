from githubkit.versions.latest.models import WebhookRepositoryArchived

from ._base import Event


class RepositoryArchived(Event):

    payload: WebhookRepositoryArchived
