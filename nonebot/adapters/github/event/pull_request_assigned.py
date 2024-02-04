from githubkit.versions.latest.models import WebhookPullRequestAssigned

from ._base import Event


class PullRequestAssigned(Event):

    payload: WebhookPullRequestAssigned
