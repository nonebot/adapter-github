from githubkit.versions.latest.models import WebhookSubIssuesParentIssueAdded

from ._base import Event


class SubIssuesParentIssueAdded(Event):
    payload: WebhookSubIssuesParentIssueAdded
