from githubkit.versions.latest.models import WebhookMarketplacePurchasePurchased

from ._base import Event


class MarketplacePurchasePurchased(Event):

    payload: WebhookMarketplacePurchasePurchased
