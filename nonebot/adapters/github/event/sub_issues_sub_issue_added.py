from githubkit.versions.latest.models import WebhookSubIssuesSubIssueAdded

from ._base import Event


class SubIssuesSubIssueAdded(Event):
    payload: WebhookSubIssuesSubIssueAdded
