from githubkit.versions.latest.models import WebhookPullRequestLabeled

from ._base import Event


class PullRequestLabeled(Event):

    payload: WebhookPullRequestLabeled
