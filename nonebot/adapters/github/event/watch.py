from githubkit.versions.latest.models import WebhookWatchStarted

from ._base import Event


class WatchStarted(Event):

    payload: WebhookWatchStarted
