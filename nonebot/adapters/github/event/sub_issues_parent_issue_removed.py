from githubkit.versions.latest.models import WebhookSubIssuesParentIssueRemoved

from ._base import Event


class SubIssuesParentIssueRemoved(Event):
    payload: WebhookSubIssuesParentIssueRemoved
