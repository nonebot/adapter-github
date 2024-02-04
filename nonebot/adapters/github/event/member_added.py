from githubkit.versions.latest.models import WebhookMemberAdded

from ._base import Event


class MemberAdded(Event):

    payload: WebhookMemberAdded
