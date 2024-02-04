from githubkit.versions.latest.models import WebhookCheckRunCreated

from ._base import Event


class CheckRunCreated(Event):

    payload: WebhookCheckRunCreated
