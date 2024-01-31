from githubkit.versions.latest.models import (
    WebhookBranchProtectionRuleEdited,
    WebhookBranchProtectionRuleCreated,
    WebhookBranchProtectionRuleDeleted,
)

from ._base import Event


class BranchProtectionRuleCreated(Event):

    payload: WebhookBranchProtectionRuleCreated


class BranchProtectionRuleDeleted(Event):

    payload: WebhookBranchProtectionRuleDeleted


class BranchProtectionRuleEdited(Event):

    payload: WebhookBranchProtectionRuleEdited
