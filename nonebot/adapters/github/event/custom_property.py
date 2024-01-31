from githubkit.versions.latest.models import (
    WebhookCustomPropertyCreated,
    WebhookCustomPropertyDeleted,
    WebhookCustomPropertyUpdated,
)

from ._base import Event


class CustomPropertyCreated(Event):

    payload: WebhookCustomPropertyCreated


class CustomPropertyDeleted(Event):

    payload: WebhookCustomPropertyDeleted


class CustomPropertyUpdated(Event):

    payload: WebhookCustomPropertyUpdated
