from githubkit.versions.latest.models import WebhookPackagePublished

from ._base import Event


class PackagePublished(Event):

    payload: WebhookPackagePublished
