from githubkit.versions.latest.models import (
    WebhookSecurityAdvisoryUpdated,
    WebhookSecurityAdvisoryPublished,
    WebhookSecurityAdvisoryWithdrawn,
)

from ._base import Event


class SecurityAdvisoryPublished(Event):

    payload: WebhookSecurityAdvisoryPublished


class SecurityAdvisoryUpdated(Event):

    payload: WebhookSecurityAdvisoryUpdated


class SecurityAdvisoryWithdrawn(Event):

    payload: WebhookSecurityAdvisoryWithdrawn
