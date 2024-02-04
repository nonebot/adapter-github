from githubkit.versions.latest.models import WebhookIssuesEdited

from ._base import Event


class IssuesEdited(Event):

    payload: WebhookIssuesEdited
