from githubkit.versions.latest.models import WebhookIssuesTransferred

from ._base import Event


class IssuesTransferred(Event):

    payload: WebhookIssuesTransferred
