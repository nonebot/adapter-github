from githubkit.versions.latest.models import WebhookMemberEdited

from ._base import Event


class MemberEdited(Event):

    payload: WebhookMemberEdited
