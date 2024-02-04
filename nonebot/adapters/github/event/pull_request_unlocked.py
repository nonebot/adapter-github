from githubkit.versions.latest.models import WebhookPullRequestUnlocked

from ._base import Event


class PullRequestUnlocked(Event):

    payload: WebhookPullRequestUnlocked
