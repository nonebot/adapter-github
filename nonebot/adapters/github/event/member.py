from githubkit.versions.latest.models import (
    WebhookMemberAdded,
    WebhookMemberEdited,
    WebhookMemberRemoved,
)

from ._base import Event


class MemberAdded(Event):

    payload: WebhookMemberAdded


class MemberEdited(Event):

    payload: WebhookMemberEdited


class MemberRemoved(Event):

    payload: WebhookMemberRemoved
