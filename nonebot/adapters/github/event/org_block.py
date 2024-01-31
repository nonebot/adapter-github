from githubkit.versions.latest.models import (
    WebhookOrgBlockBlocked,
    WebhookOrgBlockUnblocked,
)

from ._base import Event


class OrgBlockBlocked(Event):

    payload: WebhookOrgBlockBlocked


class OrgBlockUnblocked(Event):

    payload: WebhookOrgBlockUnblocked
