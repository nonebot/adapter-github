from githubkit.versions.latest.models import WebhookPersonalAccessTokenRequestDenied

from ._base import Event


class PersonalAccessTokenRequestDenied(Event):

    payload: WebhookPersonalAccessTokenRequestDenied
