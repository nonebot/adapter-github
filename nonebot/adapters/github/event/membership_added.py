from githubkit.versions.latest.models import WebhookMembershipAdded

from ._base import Event


class MembershipAdded(Event):

    payload: WebhookMembershipAdded
