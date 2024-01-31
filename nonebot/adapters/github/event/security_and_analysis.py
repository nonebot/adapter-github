from githubkit.versions.latest.models import WebhookSecurityAndAnalysis

from ._base import Event


class SecurityAndAnalysis(Event):

    payload: WebhookSecurityAndAnalysis
