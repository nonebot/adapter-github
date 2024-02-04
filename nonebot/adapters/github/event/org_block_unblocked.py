from githubkit.versions.latest.models import WebhookOrgBlockUnblocked

from ._base import Event


class OrgBlockUnblocked(Event):

    payload: WebhookOrgBlockUnblocked
