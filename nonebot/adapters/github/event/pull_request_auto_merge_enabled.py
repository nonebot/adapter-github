from githubkit.versions.latest.models import WebhookPullRequestAutoMergeEnabled

from ._base import Event


class PullRequestAutoMergeEnabled(Event):

    payload: WebhookPullRequestAutoMergeEnabled
