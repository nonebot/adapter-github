from githubkit.versions.latest.models import WebhookCheckRunCompleted

from ._base import Event


class CheckRunCompleted(Event):

    payload: WebhookCheckRunCompleted
