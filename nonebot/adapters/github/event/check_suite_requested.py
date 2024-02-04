from githubkit.versions.latest.models import WebhookCheckSuiteRequested

from ._base import Event


class CheckSuiteRequested(Event):

    payload: WebhookCheckSuiteRequested
