from githubkit.versions.latest.models import WebhookSecurityAdvisoryPublished

from ._base import Event


class SecurityAdvisoryPublished(Event):

    payload: WebhookSecurityAdvisoryPublished
