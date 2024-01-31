from githubkit.versions.latest.models import WebhookRepositoryImport

from ._base import Event


class RepositoryImport(Event):

    payload: WebhookRepositoryImport
