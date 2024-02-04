from githubkit.versions.latest.models import WebhookIssuesMilestoned

from ._base import Event


class IssuesMilestoned(Event):

    payload: WebhookIssuesMilestoned
