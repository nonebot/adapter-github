from githubkit.versions.latest.models import WebhookOrgBlockBlocked

from ._base import Event


class OrgBlockBlocked(Event):

    payload: WebhookOrgBlockBlocked
