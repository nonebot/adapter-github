from githubkit.versions.latest.models import WebhookIssuesDeleted

from ._base import Event


class IssuesDeleted(Event):

    payload: WebhookIssuesDeleted
