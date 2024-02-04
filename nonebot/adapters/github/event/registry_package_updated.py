from githubkit.versions.latest.models import WebhookRegistryPackageUpdated

from ._base import Event


class RegistryPackageUpdated(Event):

    payload: WebhookRegistryPackageUpdated
