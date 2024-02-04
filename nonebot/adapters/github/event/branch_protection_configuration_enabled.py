from githubkit.versions.latest.models import WebhookBranchProtectionConfigurationEnabled

from ._base import Event


class BranchProtectionConfigurationEnabled(Event):

    payload: WebhookBranchProtectionConfigurationEnabled
