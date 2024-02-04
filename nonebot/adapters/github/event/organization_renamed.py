from githubkit.versions.latest.models import WebhookOrganizationRenamed

from ._base import Event


class OrganizationRenamed(Event):

    payload: WebhookOrganizationRenamed
