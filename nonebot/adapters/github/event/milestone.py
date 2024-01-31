from githubkit.versions.latest.models import (
    WebhookMilestoneClosed,
    WebhookMilestoneEdited,
    WebhookMilestoneOpened,
    WebhookMilestoneCreated,
    WebhookMilestoneDeleted,
)

from ._base import Event


class MilestoneClosed(Event):

    payload: WebhookMilestoneClosed


class MilestoneCreated(Event):

    payload: WebhookMilestoneCreated


class MilestoneDeleted(Event):

    payload: WebhookMilestoneDeleted


class MilestoneEdited(Event):

    payload: WebhookMilestoneEdited


class MilestoneOpened(Event):

    payload: WebhookMilestoneOpened
