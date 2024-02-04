from githubkit.versions.latest.models import WebhookPullRequestClosed

from ._base import Event


class PullRequestClosed(Event):

    payload: WebhookPullRequestClosed
