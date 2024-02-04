from githubkit.versions.latest.models import WebhookMilestoneOpened

from ._base import Event


class MilestoneOpened(Event):

    payload: WebhookMilestoneOpened
