from githubkit.versions.latest.models import WebhookIssuesUnlocked

from ._base import Event


class IssuesUnlocked(Event):

    payload: WebhookIssuesUnlocked
