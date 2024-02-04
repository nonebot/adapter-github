from githubkit.versions.latest.models import WebhookPullRequestUnlabeled

from ._base import Event


class PullRequestUnlabeled(Event):

    payload: WebhookPullRequestUnlabeled
