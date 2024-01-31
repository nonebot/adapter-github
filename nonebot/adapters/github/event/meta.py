from githubkit.versions.latest.models import WebhookMetaDeleted

from ._base import Event


class MetaDeleted(Event):

    payload: WebhookMetaDeleted
