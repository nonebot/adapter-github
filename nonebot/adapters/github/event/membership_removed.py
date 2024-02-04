from githubkit.versions.latest.models import WebhookMembershipRemoved

from ._base import Event


class MembershipRemoved(Event):

    payload: WebhookMembershipRemoved
