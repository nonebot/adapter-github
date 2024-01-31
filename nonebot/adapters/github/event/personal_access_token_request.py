from githubkit.versions.latest.models import (
    WebhookPersonalAccessTokenRequestDenied,
    WebhookPersonalAccessTokenRequestCreated,
    WebhookPersonalAccessTokenRequestApproved,
    WebhookPersonalAccessTokenRequestCancelled,
)

from ._base import Event


class PersonalAccessTokenRequestApproved(Event):

    payload: WebhookPersonalAccessTokenRequestApproved


class PersonalAccessTokenRequestCancelled(Event):

    payload: WebhookPersonalAccessTokenRequestCancelled


class PersonalAccessTokenRequestCreated(Event):

    payload: WebhookPersonalAccessTokenRequestCreated


class PersonalAccessTokenRequestDenied(Event):

    payload: WebhookPersonalAccessTokenRequestDenied
