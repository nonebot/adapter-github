from githubkit.versions.latest.models import (
    WebhookRepositoryRulesetEdited,
    WebhookRepositoryRulesetCreated,
    WebhookRepositoryRulesetDeleted,
)

from ._base import Event


class RepositoryRulesetCreated(Event):

    payload: WebhookRepositoryRulesetCreated


class RepositoryRulesetDeleted(Event):

    payload: WebhookRepositoryRulesetDeleted


class RepositoryRulesetEdited(Event):

    payload: WebhookRepositoryRulesetEdited
