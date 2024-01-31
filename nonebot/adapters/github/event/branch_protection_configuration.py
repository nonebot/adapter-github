from githubkit.versions.latest.models import (
    WebhookBranchProtectionConfigurationEnabled,
    WebhookBranchProtectionConfigurationDisabled,
)

from ._base import Event


class BranchProtectionConfigurationDisabled(Event):

    payload: WebhookBranchProtectionConfigurationDisabled


class BranchProtectionConfigurationEnabled(Event):

    payload: WebhookBranchProtectionConfigurationEnabled
