from githubkit.versions.latest.models import WebhookBranchProtectionRuleEdited

from ._base import Event


class BranchProtectionRuleEdited(Event):

    payload: WebhookBranchProtectionRuleEdited
