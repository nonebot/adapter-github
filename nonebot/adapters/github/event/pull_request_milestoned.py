from githubkit.versions.latest.models import WebhookPullRequestMilestoned

from ._base import Event


class PullRequestMilestoned(Event):

    payload: WebhookPullRequestMilestoned
