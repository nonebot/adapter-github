from githubkit.versions.latest.models import WebhookIssuesLocked

from ._base import Event


class IssuesLocked(Event):

    payload: WebhookIssuesLocked
