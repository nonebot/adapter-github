from githubkit.versions.latest.models import WebhookPullRequestDequeued

from ._base import Event


class PullRequestDequeued(Event):

    payload: WebhookPullRequestDequeued
