from githubkit.versions.latest.models import (
    WebhookRepositoryAdvisoryReported,
    WebhookRepositoryAdvisoryPublished,
)

from ._base import Event


class RepositoryAdvisoryPublished(Event):

    payload: WebhookRepositoryAdvisoryPublished


class RepositoryAdvisoryReported(Event):

    payload: WebhookRepositoryAdvisoryReported
