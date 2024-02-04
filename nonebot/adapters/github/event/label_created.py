from githubkit.versions.latest.models import WebhookLabelCreated

from ._base import Event


class LabelCreated(Event):

    payload: WebhookLabelCreated
