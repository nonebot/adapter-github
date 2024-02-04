from githubkit.versions.latest.models import WebhookOrganizationMemberInvited

from ._base import Event


class OrganizationMemberInvited(Event):

    payload: WebhookOrganizationMemberInvited
