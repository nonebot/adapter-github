from githubkit.versions.latest.models import WebhookPullRequestOpened

from ._base import Event


class PullRequestOpened(Event):

    payload: WebhookPullRequestOpened
