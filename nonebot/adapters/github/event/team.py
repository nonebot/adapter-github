from githubkit.versions.latest.models import (
    WebhookTeamEdited,
    WebhookTeamCreated,
    WebhookTeamDeleted,
    WebhookTeamAddedToRepository,
    WebhookTeamRemovedFromRepository,
)

from ._base import Event


class TeamAddedToRepository(Event):

    payload: WebhookTeamAddedToRepository


class TeamCreated(Event):

    payload: WebhookTeamCreated


class TeamDeleted(Event):

    payload: WebhookTeamDeleted


class TeamEdited(Event):

    payload: WebhookTeamEdited


class TeamRemovedFromRepository(Event):

    payload: WebhookTeamRemovedFromRepository
