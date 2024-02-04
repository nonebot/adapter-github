from githubkit.versions.latest.models import WebhookIssuesUnpinned

from ._base import Event


class IssuesUnpinned(Event):

    payload: WebhookIssuesUnpinned
