from githubkit.versions.latest.models import WebhookIssueDependenciesBlockedByAdded

from ._base import Event


class IssueDependenciesBlockedByAdded(Event):
    payload: WebhookIssueDependenciesBlockedByAdded
