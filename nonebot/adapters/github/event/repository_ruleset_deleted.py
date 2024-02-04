from githubkit.versions.latest.models import WebhookRepositoryRulesetDeleted

from ._base import Event


class RepositoryRulesetDeleted(Event):

    payload: WebhookRepositoryRulesetDeleted
