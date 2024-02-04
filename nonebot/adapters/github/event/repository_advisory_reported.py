from githubkit.versions.latest.models import WebhookRepositoryAdvisoryReported

from ._base import Event


class RepositoryAdvisoryReported(Event):

    payload: WebhookRepositoryAdvisoryReported
