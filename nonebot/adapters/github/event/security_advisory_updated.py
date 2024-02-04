from githubkit.versions.latest.models import WebhookSecurityAdvisoryUpdated

from ._base import Event


class SecurityAdvisoryUpdated(Event):

    payload: WebhookSecurityAdvisoryUpdated
