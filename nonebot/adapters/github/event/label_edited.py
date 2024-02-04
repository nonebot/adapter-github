from githubkit.versions.latest.models import WebhookLabelEdited

from ._base import Event


class LabelEdited(Event):

    payload: WebhookLabelEdited
