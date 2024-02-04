from githubkit.versions.latest.models import WebhookRepositoryEdited

from ._base import Event


class RepositoryEdited(Event):

    payload: WebhookRepositoryEdited
