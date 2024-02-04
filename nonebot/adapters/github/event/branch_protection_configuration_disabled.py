from githubkit.versions.latest.models import (
    WebhookBranchProtectionConfigurationDisabled,
)

from ._base import Event


class BranchProtectionConfigurationDisabled(Event):

    payload: WebhookBranchProtectionConfigurationDisabled
