from githubkit.versions.latest.models import WebhookIssuesAssigned

from ._base import Event


class IssuesAssigned(Event):

    payload: WebhookIssuesAssigned
