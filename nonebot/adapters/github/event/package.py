from githubkit.versions.latest.models import (
    WebhookPackageUpdated,
    WebhookPackagePublished,
)

from ._base import Event


class PackagePublished(Event):

    payload: WebhookPackagePublished


class PackageUpdated(Event):

    payload: WebhookPackageUpdated
