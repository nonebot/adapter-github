from githubkit.versions.latest.models import WebhookRegistryPackagePublished

from ._base import Event


class RegistryPackagePublished(Event):

    payload: WebhookRegistryPackagePublished
