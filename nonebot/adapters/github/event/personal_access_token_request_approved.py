from githubkit.versions.latest.models import WebhookPersonalAccessTokenRequestApproved

from ._base import Event


class PersonalAccessTokenRequestApproved(Event):

    payload: WebhookPersonalAccessTokenRequestApproved
