from githubkit.versions.latest.models import WebhookPersonalAccessTokenRequestCancelled

from ._base import Event


class PersonalAccessTokenRequestCancelled(Event):

    payload: WebhookPersonalAccessTokenRequestCancelled
