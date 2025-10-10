from githubkit.versions.latest.models import WebhookIssueDependenciesBlockingRemoved

from ._base import Event


class IssueDependenciesBlockingRemoved(Event):
    payload: WebhookIssueDependenciesBlockingRemoved
