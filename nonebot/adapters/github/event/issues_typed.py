from githubkit.versions.latest.models import WebhookIssuesTyped

from ._base import Event


class IssuesTyped(Event):
    payload: WebhookIssuesTyped
