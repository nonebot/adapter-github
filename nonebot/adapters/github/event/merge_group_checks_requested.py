from githubkit.versions.latest.models import WebhookMergeGroupChecksRequested

from ._base import Event


class MergeGroupChecksRequested(Event):

    payload: WebhookMergeGroupChecksRequested
