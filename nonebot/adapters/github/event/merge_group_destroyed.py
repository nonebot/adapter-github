from githubkit.versions.latest.models import WebhookMergeGroupDestroyed

from ._base import Event


class MergeGroupDestroyed(Event):

    payload: WebhookMergeGroupDestroyed
