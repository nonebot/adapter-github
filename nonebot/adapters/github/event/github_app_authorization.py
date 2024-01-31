from githubkit.versions.latest.models import WebhookGithubAppAuthorizationRevoked

from ._base import Event


class GithubAppAuthorizationRevoked(Event):

    payload: WebhookGithubAppAuthorizationRevoked
