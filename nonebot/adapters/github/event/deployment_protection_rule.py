from githubkit.versions.latest.models import WebhookDeploymentProtectionRuleRequested

from ._base import Event


class DeploymentProtectionRuleRequested(Event):

    payload: WebhookDeploymentProtectionRuleRequested
