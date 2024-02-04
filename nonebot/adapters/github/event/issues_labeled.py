from githubkit.versions.latest.models import WebhookIssuesLabeled

from ._base import Event


class IssuesLabeled(Event):

    payload: WebhookIssuesLabeled
