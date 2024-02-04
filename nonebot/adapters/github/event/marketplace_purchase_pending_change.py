from githubkit.versions.latest.models import WebhookMarketplacePurchasePendingChange

from ._base import Event


class MarketplacePurchasePendingChange(Event):

    payload: WebhookMarketplacePurchasePendingChange
