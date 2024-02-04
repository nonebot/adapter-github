from githubkit.versions.latest.models import WebhookDependabotAlertAutoDismissed

from ._base import Event


class DependabotAlertAutoDismissed(Event):

    payload: WebhookDependabotAlertAutoDismissed
