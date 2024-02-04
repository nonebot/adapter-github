from githubkit.versions.latest.models import WebhookSecurityAdvisoryWithdrawn

from ._base import Event


class SecurityAdvisoryWithdrawn(Event):

    payload: WebhookSecurityAdvisoryWithdrawn
