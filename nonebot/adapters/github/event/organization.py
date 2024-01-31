from githubkit.versions.latest.models import (
    WebhookOrganizationDeleted,
    WebhookOrganizationRenamed,
    WebhookOrganizationMemberAdded,
    WebhookOrganizationMemberInvited,
    WebhookOrganizationMemberRemoved,
)

from ._base import Event


class OrganizationDeleted(Event):

    payload: WebhookOrganizationDeleted


class OrganizationMemberAdded(Event):

    payload: WebhookOrganizationMemberAdded


class OrganizationMemberInvited(Event):

    payload: WebhookOrganizationMemberInvited


class OrganizationMemberRemoved(Event):

    payload: WebhookOrganizationMemberRemoved


class OrganizationRenamed(Event):

    payload: WebhookOrganizationRenamed
