from githubkit.versions.latest.models import WebhookIssuesDemilestoned

from ._base import Event


class IssuesDemilestoned(Event):

    payload: WebhookIssuesDemilestoned
