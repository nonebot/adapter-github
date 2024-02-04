from githubkit.versions.latest.models import WebhookIssuesUnlabeled

from ._base import Event


class IssuesUnlabeled(Event):

    payload: WebhookIssuesUnlabeled
