from githubkit.versions.latest.models import WebhookMarketplacePurchaseChanged

from ._base import Event


class MarketplacePurchaseChanged(Event):

    payload: WebhookMarketplacePurchaseChanged
