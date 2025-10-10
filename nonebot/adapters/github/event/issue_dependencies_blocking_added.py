from githubkit.versions.latest.models import WebhookIssueDependenciesBlockingAdded

from ._base import Event


class IssueDependenciesBlockingAdded(Event):
    payload: WebhookIssueDependenciesBlockingAdded
