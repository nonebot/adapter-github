from githubkit.versions.latest.models import WebhookRepositoryRulesetCreated

from ._base import Event


class RepositoryRulesetCreated(Event):

    payload: WebhookRepositoryRulesetCreated
