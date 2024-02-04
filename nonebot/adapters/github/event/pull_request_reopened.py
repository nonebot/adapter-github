from githubkit.versions.latest.models import WebhookPullRequestReopened

from ._base import Event


class PullRequestReopened(Event):

    payload: WebhookPullRequestReopened
