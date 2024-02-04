from githubkit.versions.latest.models import WebhookTeamEdited

from ._base import Event


class TeamEdited(Event):

    payload: WebhookTeamEdited
