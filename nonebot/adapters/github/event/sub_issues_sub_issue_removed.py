from githubkit.versions.latest.models import WebhookSubIssuesSubIssueRemoved

from ._base import Event


class SubIssuesSubIssueRemoved(Event):
    payload: WebhookSubIssuesSubIssueRemoved
