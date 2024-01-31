from githubkit.versions.latest.models import (
    WebhookMembershipAdded,
    WebhookMembershipRemoved,
)

from ._base import Event


class MembershipAdded(Event):

    payload: WebhookMembershipAdded


class MembershipRemoved(Event):

    payload: WebhookMembershipRemoved
