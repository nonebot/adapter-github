from githubkit.versions.latest.models import WebhookTeamAdd

from ._base import Event


class TeamAdd(Event):

    payload: WebhookTeamAdd
