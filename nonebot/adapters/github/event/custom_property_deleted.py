from githubkit.versions.latest.models import WebhookCustomPropertyDeleted

from ._base import Event


class CustomPropertyDeleted(Event):

    payload: WebhookCustomPropertyDeleted
