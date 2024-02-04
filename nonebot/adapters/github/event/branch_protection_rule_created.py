from githubkit.versions.latest.models import WebhookBranchProtectionRuleCreated

from ._base import Event


class BranchProtectionRuleCreated(Event):

    payload: WebhookBranchProtectionRuleCreated
