from githubkit.versions.latest.models import WebhookPullRequestLocked

from ._base import Event


class PullRequestLocked(Event):

    payload: WebhookPullRequestLocked
