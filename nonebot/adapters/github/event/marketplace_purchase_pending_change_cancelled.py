from githubkit.versions.latest.models import (
    WebhookMarketplacePurchasePendingChangeCancelled,
)

from ._base import Event


class MarketplacePurchasePendingChangeCancelled(Event):

    payload: WebhookMarketplacePurchasePendingChangeCancelled
