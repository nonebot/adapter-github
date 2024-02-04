from githubkit.versions.latest.models import WebhookIssuesUnassigned

from ._base import Event


class IssuesUnassigned(Event):

    payload: WebhookIssuesUnassigned
