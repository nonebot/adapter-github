from githubkit.versions.latest.models import WebhookIssueDependenciesBlockedByRemoved

from ._base import Event


class IssueDependenciesBlockedByRemoved(Event):
    payload: WebhookIssueDependenciesBlockedByRemoved
