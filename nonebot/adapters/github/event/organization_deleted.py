from githubkit.versions.latest.models import WebhookOrganizationDeleted

from ._base import Event


class OrganizationDeleted(Event):

    payload: WebhookOrganizationDeleted
