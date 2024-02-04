from githubkit.versions.latest.models import WebhookPullRequestDemilestoned

from ._base import Event


class PullRequestDemilestoned(Event):

    payload: WebhookPullRequestDemilestoned
