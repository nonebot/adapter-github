from githubkit.versions.latest.models import WebhookPullRequestEnqueued

from ._base import Event


class PullRequestEnqueued(Event):

    payload: WebhookPullRequestEnqueued
