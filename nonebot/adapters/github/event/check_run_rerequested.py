from githubkit.versions.latest.models import WebhookCheckRunRerequested

from ._base import Event


class CheckRunRerequested(Event):

    payload: WebhookCheckRunRerequested
