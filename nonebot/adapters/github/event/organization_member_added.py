from githubkit.versions.latest.models import WebhookOrganizationMemberAdded

from ._base import Event


class OrganizationMemberAdded(Event):

    payload: WebhookOrganizationMemberAdded
