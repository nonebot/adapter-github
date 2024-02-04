from githubkit.versions.latest.models import WebhookBranchProtectionRuleDeleted

from ._base import Event


class BranchProtectionRuleDeleted(Event):

    payload: WebhookBranchProtectionRuleDeleted
