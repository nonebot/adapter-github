from githubkit.versions.latest.models import WebhookPackageUpdated

from ._base import Event


class PackageUpdated(Event):

    payload: WebhookPackageUpdated
