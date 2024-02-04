from githubkit.versions.latest.models import WebhookMemberRemoved

from ._base import Event


class MemberRemoved(Event):

    payload: WebhookMemberRemoved
