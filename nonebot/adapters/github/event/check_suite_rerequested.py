from githubkit.versions.latest.models import WebhookCheckSuiteRerequested

from ._base import Event


class CheckSuiteRerequested(Event):

    payload: WebhookCheckSuiteRerequested
