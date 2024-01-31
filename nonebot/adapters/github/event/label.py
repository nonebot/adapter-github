from githubkit.versions.latest.models import (
    WebhookLabelEdited,
    WebhookLabelCreated,
    WebhookLabelDeleted,
)

from ._base import Event


class LabelCreated(Event):

    payload: WebhookLabelCreated


class LabelDeleted(Event):

    payload: WebhookLabelDeleted


class LabelEdited(Event):

    payload: WebhookLabelEdited
