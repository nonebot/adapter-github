from githubkit.versions.latest.models import WebhookPullRequestAutoMergeDisabled

from ._base import Event


class PullRequestAutoMergeDisabled(Event):

    payload: WebhookPullRequestAutoMergeDisabled
