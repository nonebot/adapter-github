from githubkit.versions.latest.models import WebhookMilestoneEdited

from ._base import Event


class MilestoneEdited(Event):

    payload: WebhookMilestoneEdited
