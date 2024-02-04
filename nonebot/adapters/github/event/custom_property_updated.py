from githubkit.versions.latest.models import WebhookCustomPropertyUpdated

from ._base import Event


class CustomPropertyUpdated(Event):

    payload: WebhookCustomPropertyUpdated
