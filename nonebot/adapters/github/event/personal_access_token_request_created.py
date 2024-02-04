from githubkit.versions.latest.models import WebhookPersonalAccessTokenRequestCreated

from ._base import Event


class PersonalAccessTokenRequestCreated(Event):

    payload: WebhookPersonalAccessTokenRequestCreated
