from githubkit.versions.latest.models import WebhookRepositoryPrivatized

from ._base import Event


class RepositoryPrivatized(Event):

    payload: WebhookRepositoryPrivatized
