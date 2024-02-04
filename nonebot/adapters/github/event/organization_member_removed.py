from githubkit.versions.latest.models import WebhookOrganizationMemberRemoved

from ._base import Event


class OrganizationMemberRemoved(Event):

    payload: WebhookOrganizationMemberRemoved
