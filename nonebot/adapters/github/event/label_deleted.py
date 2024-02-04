from githubkit.versions.latest.models import WebhookLabelDeleted

from ._base import Event


class LabelDeleted(Event):

    payload: WebhookLabelDeleted
