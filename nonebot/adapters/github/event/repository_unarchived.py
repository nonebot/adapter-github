from githubkit.versions.latest.models import WebhookRepositoryUnarchived

from ._base import Event


class RepositoryUnarchived(Event):

    payload: WebhookRepositoryUnarchived
