from githubkit.versions.latest.models import WebhookMarketplacePurchaseCancelled

from ._base import Event


class MarketplacePurchaseCancelled(Event):

    payload: WebhookMarketplacePurchaseCancelled
