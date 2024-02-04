from githubkit.versions.latest.models import WebhookCheckSuiteCompleted

from ._base import Event


class CheckSuiteCompleted(Event):

    payload: WebhookCheckSuiteCompleted
