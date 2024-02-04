from githubkit.versions.latest.models import WebhookTeamRemovedFromRepository

from ._base import Event


class TeamRemovedFromRepository(Event):

    payload: WebhookTeamRemovedFromRepository
