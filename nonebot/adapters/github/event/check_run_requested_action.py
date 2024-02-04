from githubkit.versions.latest.models import WebhookCheckRunRequestedAction

from ._base import Event


class CheckRunRequestedAction(Event):

    payload: WebhookCheckRunRequestedAction
