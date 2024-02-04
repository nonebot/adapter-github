from githubkit.versions.latest.models import WebhookIssuesPinned

from ._base import Event


class IssuesPinned(Event):

    payload: WebhookIssuesPinned
