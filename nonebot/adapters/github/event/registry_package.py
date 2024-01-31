from githubkit.versions.latest.models import (
    WebhookRegistryPackageUpdated,
    WebhookRegistryPackagePublished,
)

from ._base import Event


class RegistryPackagePublished(Event):

    payload: WebhookRegistryPackagePublished


class RegistryPackageUpdated(Event):

    payload: WebhookRegistryPackageUpdated
