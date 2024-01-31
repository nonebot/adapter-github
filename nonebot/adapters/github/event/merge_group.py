from githubkit.versions.latest.models import (
    WebhookMergeGroupDestroyed,
    WebhookMergeGroupChecksRequested,
)

from ._base import Event


class MergeGroupChecksRequested(Event):

    payload: WebhookMergeGroupChecksRequested


class MergeGroupDestroyed(Event):

    payload: WebhookMergeGroupDestroyed
