from githubkit.versions.latest.models import (
    WebhookMarketplacePurchaseChanged,
    WebhookMarketplacePurchaseCancelled,
    WebhookMarketplacePurchasePurchased,
    WebhookMarketplacePurchasePendingChange,
    WebhookMarketplacePurchasePendingChangeCancelled,
)

from ._base import Event


class MarketplacePurchaseCancelled(Event):

    payload: WebhookMarketplacePurchaseCancelled


class MarketplacePurchaseChanged(Event):

    payload: WebhookMarketplacePurchaseChanged


class MarketplacePurchasePendingChange(Event):

    payload: WebhookMarketplacePurchasePendingChange


class MarketplacePurchasePendingChangeCancelled(Event):

    payload: WebhookMarketplacePurchasePendingChangeCancelled


class MarketplacePurchasePurchased(Event):

    payload: WebhookMarketplacePurchasePurchased
