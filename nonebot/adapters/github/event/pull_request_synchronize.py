from githubkit.versions.latest.models import WebhookPullRequestSynchronize

from ._base import Event


class PullRequestSynchronize(Event):

    payload: WebhookPullRequestSynchronize
