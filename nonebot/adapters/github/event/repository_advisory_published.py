from githubkit.versions.latest.models import WebhookRepositoryAdvisoryPublished

from ._base import Event


class RepositoryAdvisoryPublished(Event):

    payload: WebhookRepositoryAdvisoryPublished
