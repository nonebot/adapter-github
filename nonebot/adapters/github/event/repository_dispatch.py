from githubkit.versions.latest.models import WebhookRepositoryDispatchSample

from ._base import Event


class RepositoryDispatchSample(Event):

    payload: WebhookRepositoryDispatchSample
