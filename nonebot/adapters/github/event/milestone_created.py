from githubkit.versions.latest.models import WebhookMilestoneCreated

from ._base import Event


class MilestoneCreated(Event):

    payload: WebhookMilestoneCreated
