from githubkit.versions.latest.models import WebhookRepositoryPublicized

from ._base import Event


class RepositoryPublicized(Event):

    payload: WebhookRepositoryPublicized
