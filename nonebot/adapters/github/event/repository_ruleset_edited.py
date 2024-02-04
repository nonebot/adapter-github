from githubkit.versions.latest.models import WebhookRepositoryRulesetEdited

from ._base import Event


class RepositoryRulesetEdited(Event):

    payload: WebhookRepositoryRulesetEdited
