from githubkit.versions.latest.models import WebhookIssuesOpened

from ._base import Event


class IssuesOpened(Event):

    payload: WebhookIssuesOpened
