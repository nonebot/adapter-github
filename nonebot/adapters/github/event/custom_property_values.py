from githubkit.versions.latest.models import WebhookCustomPropertyValuesUpdated

from ._base import Event


class CustomPropertyValuesUpdated(Event):

    payload: WebhookCustomPropertyValuesUpdated
