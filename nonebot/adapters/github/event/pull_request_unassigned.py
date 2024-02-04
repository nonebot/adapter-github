from githubkit.versions.latest.models import WebhookPullRequestUnassigned

from ._base import Event


class PullRequestUnassigned(Event):

    payload: WebhookPullRequestUnassigned
