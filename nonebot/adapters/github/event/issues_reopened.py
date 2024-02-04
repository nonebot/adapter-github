from githubkit.versions.latest.models import WebhookIssuesReopened

from ._base import Event


class IssuesReopened(Event):

    payload: WebhookIssuesReopened
