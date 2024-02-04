from githubkit.versions.latest.models import WebhookCustomPropertyCreated

from ._base import Event


class CustomPropertyCreated(Event):

    payload: WebhookCustomPropertyCreated
