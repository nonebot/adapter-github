from githubkit.versions.latest.models import WebhookIssuesClosed

from ._base import Event


class IssuesClosed(Event):

    payload: WebhookIssuesClosed
