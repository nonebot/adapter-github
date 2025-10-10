from githubkit.versions.latest.models import WebhookCustomPropertyPromotedToEnterprise

from ._base import Event


class CustomPropertyPromotedToEnterprise(Event):
    payload: WebhookCustomPropertyPromotedToEnterprise
