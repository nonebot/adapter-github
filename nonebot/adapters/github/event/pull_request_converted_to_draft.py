from githubkit.versions.latest.models import WebhookPullRequestConvertedToDraft

from ._base import Event


class PullRequestConvertedToDraft(Event):

    payload: WebhookPullRequestConvertedToDraft
