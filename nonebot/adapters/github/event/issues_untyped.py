from githubkit.versions.latest.models import WebhookIssuesUntyped

from ._base import Event


class IssuesUntyped(Event):
    payload: WebhookIssuesUntyped
