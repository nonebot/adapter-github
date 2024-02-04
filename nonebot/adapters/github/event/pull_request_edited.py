from githubkit.versions.latest.models import WebhookPullRequestEdited

from ._base import Event


class PullRequestEdited(Event):

    payload: WebhookPullRequestEdited
