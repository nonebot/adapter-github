from githubkit.versions.latest.models import WebhookTeamDeleted

from ._base import Event


class TeamDeleted(Event):

    payload: WebhookTeamDeleted
