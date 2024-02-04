from githubkit.versions.latest.models import WebhookMilestoneDeleted

from ._base import Event


class MilestoneDeleted(Event):

    payload: WebhookMilestoneDeleted
