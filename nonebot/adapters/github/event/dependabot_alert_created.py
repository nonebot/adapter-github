from githubkit.versions.latest.models import WebhookDependabotAlertCreated

from ._base import Event


class DependabotAlertCreated(Event):

    payload: WebhookDependabotAlertCreated
