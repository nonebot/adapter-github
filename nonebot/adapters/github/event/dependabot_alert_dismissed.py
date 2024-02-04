from githubkit.versions.latest.models import WebhookDependabotAlertDismissed

from ._base import Event


class DependabotAlertDismissed(Event):

    payload: WebhookDependabotAlertDismissed
