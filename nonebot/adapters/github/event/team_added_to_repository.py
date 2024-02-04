from githubkit.versions.latest.models import WebhookTeamAddedToRepository

from ._base import Event


class TeamAddedToRepository(Event):

    payload: WebhookTeamAddedToRepository
