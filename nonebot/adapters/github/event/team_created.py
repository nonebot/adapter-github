from githubkit.versions.latest.models import WebhookTeamCreated

from ._base import Event


class TeamCreated(Event):

    payload: WebhookTeamCreated
