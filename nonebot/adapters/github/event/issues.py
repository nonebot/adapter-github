from githubkit.versions.latest.models import (
    WebhookIssuesClosed,
    WebhookIssuesEdited,
    WebhookIssuesLocked,
    WebhookIssuesOpened,
    WebhookIssuesPinned,
    WebhookIssuesDeleted,
    WebhookIssuesLabeled,
    WebhookIssuesAssigned,
    WebhookIssuesReopened,
    WebhookIssuesUnlocked,
    WebhookIssuesUnpinned,
    WebhookIssuesUnlabeled,
    WebhookIssuesMilestoned,
    WebhookIssuesUnassigned,
    WebhookIssuesTransferred,
    WebhookIssuesDemilestoned,
)

from ._base import Event


class IssuesAssigned(Event):

    payload: WebhookIssuesAssigned


class IssuesClosed(Event):

    payload: WebhookIssuesClosed


class IssuesDeleted(Event):

    payload: WebhookIssuesDeleted


class IssuesDemilestoned(Event):

    payload: WebhookIssuesDemilestoned


class IssuesEdited(Event):

    payload: WebhookIssuesEdited


class IssuesLabeled(Event):

    payload: WebhookIssuesLabeled


class IssuesLocked(Event):

    payload: WebhookIssuesLocked


class IssuesMilestoned(Event):

    payload: WebhookIssuesMilestoned


class IssuesOpened(Event):

    payload: WebhookIssuesOpened


class IssuesPinned(Event):

    payload: WebhookIssuesPinned


class IssuesReopened(Event):

    payload: WebhookIssuesReopened


class IssuesTransferred(Event):

    payload: WebhookIssuesTransferred


class IssuesUnassigned(Event):

    payload: WebhookIssuesUnassigned


class IssuesUnlabeled(Event):

    payload: WebhookIssuesUnlabeled


class IssuesUnlocked(Event):

    payload: WebhookIssuesUnlocked


class IssuesUnpinned(Event):

    payload: WebhookIssuesUnpinned
