from typing import Any, Dict, Union
from functools import cached_property

from nonebot.typing import overrides
from nonebot.utils import escape_tag
from githubkit.webhooks.models import ForkEvent as ForkEventPayload
from githubkit.webhooks.models import PingEvent as PingEventPayload
from githubkit.webhooks.models import PushEvent as PushEventPayload
from githubkit.webhooks.models import TeamEdited as TeamEditedPayload
from githubkit.webhooks.models import CreateEvent as CreateEventPayload
from githubkit.webhooks.models import DeleteEvent as DeleteEventPayload
from githubkit.webhooks.models import GollumEvent as GollumEventPayload
from githubkit.webhooks.models import LabelEdited as LabelEditedPayload
from githubkit.webhooks.models import MemberAdded as MemberAddedPayload
from githubkit.webhooks.models import MetaDeleted as MetaDeletedPayload
from githubkit.webhooks.models import PublicEvent as PublicEventPayload
from githubkit.webhooks.models import StarCreated as StarCreatedPayload
from githubkit.webhooks.models import StarDeleted as StarDeletedPayload
from githubkit.webhooks.models import StatusEvent as StatusEventPayload
from githubkit.webhooks.models import TeamCreated as TeamCreatedPayload
from githubkit.webhooks.models import TeamDeleted as TeamDeletedPayload
from githubkit.webhooks.models import IssuesClosed as IssuesClosedPayload
from githubkit.webhooks.models import IssuesEdited as IssuesEditedPayload
from githubkit.webhooks.models import IssuesLocked as IssuesLockedPayload
from githubkit.webhooks.models import IssuesOpened as IssuesOpenedPayload
from githubkit.webhooks.models import IssuesPinned as IssuesPinnedPayload
from githubkit.webhooks.models import LabelCreated as LabelCreatedPayload
from githubkit.webhooks.models import LabelDeleted as LabelDeletedPayload
from githubkit.webhooks.models import MemberEdited as MemberEditedPayload
from githubkit.webhooks.models import TeamAddEvent as TeamAddEventPayload
from githubkit.webhooks.models import WatchStarted as WatchStartedPayload
from githubkit.webhooks.models import IssuesDeleted as IssuesDeletedPayload
from githubkit.webhooks.models import IssuesLabeled as IssuesLabeledPayload
from githubkit.webhooks.models import MemberRemoved as MemberRemovedPayload
from githubkit.webhooks.models import ProjectClosed as ProjectClosedPayload
from githubkit.webhooks.models import ProjectEdited as ProjectEditedPayload
from githubkit.webhooks.models import ReleaseEdited as ReleaseEditedPayload
from githubkit.webhooks.models import IssuesAssigned as IssuesAssignedPayload
from githubkit.webhooks.models import IssuesReopened as IssuesReopenedPayload
from githubkit.webhooks.models import IssuesUnlocked as IssuesUnlockedPayload
from githubkit.webhooks.models import IssuesUnpinned as IssuesUnpinnedPayload
from githubkit.webhooks.models import PackageUpdated as PackageUpdatedPayload
from githubkit.webhooks.models import PageBuildEvent as PageBuildEventPayload
from githubkit.webhooks.models import ProjectCreated as ProjectCreatedPayload
from githubkit.webhooks.models import ProjectDeleted as ProjectDeletedPayload
from githubkit.webhooks.models import ReleaseCreated as ReleaseCreatedPayload
from githubkit.webhooks.models import ReleaseDeleted as ReleaseDeletedPayload
from githubkit.webhooks.models import CheckRunCreated as CheckRunCreatedPayload
from githubkit.webhooks.models import IssuesUnlabeled as IssuesUnlabeledPayload
from githubkit.webhooks.models import MembershipAdded as MembershipAddedPayload
from githubkit.webhooks.models import MilestoneClosed as MilestoneClosedPayload
from githubkit.webhooks.models import MilestoneEdited as MilestoneEditedPayload
from githubkit.webhooks.models import MilestoneOpened as MilestoneOpenedPayload
from githubkit.webhooks.models import OrgBlockBlocked as OrgBlockBlockedPayload
from githubkit.webhooks.models import ProjectReopened as ProjectReopenedPayload
from githubkit.webhooks.models import ReleaseReleased as ReleaseReleasedPayload
from githubkit.webhooks.models import DeployKeyCreated as DeployKeyCreatedPayload
from githubkit.webhooks.models import DeployKeyDeleted as DeployKeyDeletedPayload
from githubkit.webhooks.models import DiscussionEdited as DiscussionEditedPayload
from githubkit.webhooks.models import DiscussionLocked as DiscussionLockedPayload
from githubkit.webhooks.models import DiscussionPinned as DiscussionPinnedPayload
from githubkit.webhooks.models import IssuesMilestoned as IssuesMilestonedPayload
from githubkit.webhooks.models import IssuesUnassigned as IssuesUnassignedPayload
from githubkit.webhooks.models import MilestoneCreated as MilestoneCreatedPayload
from githubkit.webhooks.models import MilestoneDeleted as MilestoneDeletedPayload
from githubkit.webhooks.models import PackagePublished as PackagePublishedPayload
from githubkit.webhooks.models import ProjectCardMoved as ProjectCardMovedPayload
from githubkit.webhooks.models import ReleasePublished as ReleasePublishedPayload
from githubkit.webhooks.models import RepositoryEdited as RepositoryEditedPayload
from githubkit.webhooks.models import CheckRunCompleted as CheckRunCompletedPayload
from githubkit.webhooks.models import DeploymentCreated as DeploymentCreatedPayload
from githubkit.webhooks.models import DiscussionCreated as DiscussionCreatedPayload
from githubkit.webhooks.models import DiscussionDeleted as DiscussionDeletedPayload
from githubkit.webhooks.models import DiscussionLabeled as DiscussionLabeledPayload
from githubkit.webhooks.models import IssuesTransferred as IssuesTransferredPayload
from githubkit.webhooks.models import MembershipRemoved as MembershipRemovedPayload
from githubkit.webhooks.models import OrgBlockUnblocked as OrgBlockUnblockedPayload
from githubkit.webhooks.models import ProjectCardEdited as ProjectCardEditedPayload
from githubkit.webhooks.models import PullRequestClosed as PullRequestClosedPayload
from githubkit.webhooks.models import PullRequestEdited as PullRequestEditedPayload
from githubkit.webhooks.models import PullRequestLocked as PullRequestLockedPayload
from githubkit.webhooks.models import PullRequestOpened as PullRequestOpenedPayload
from githubkit.webhooks.models import RepositoryCreated as RepositoryCreatedPayload
from githubkit.webhooks.models import RepositoryDeleted as RepositoryDeletedPayload
from githubkit.webhooks.models import RepositoryRenamed as RepositoryRenamedPayload
from githubkit.webhooks.models import SponsorshipEdited as SponsorshipEditedPayload
from githubkit.webhooks.models import WorkflowJobQueued as WorkflowJobQueuedPayload
from githubkit.webhooks.models import DiscussionAnswered as DiscussionAnsweredPayload
from githubkit.webhooks.models import DiscussionUnlocked as DiscussionUnlockedPayload
from githubkit.webhooks.models import DiscussionUnpinned as DiscussionUnpinnedPayload
from githubkit.webhooks.models import IssueCommentEdited as IssueCommentEditedPayload
from githubkit.webhooks.models import IssuesDemilestoned as IssuesDemilestonedPayload
from githubkit.webhooks.models import ProjectCardCreated as ProjectCardCreatedPayload
from githubkit.webhooks.models import ProjectCardDeleted as ProjectCardDeletedPayload
from githubkit.webhooks.models import ProjectColumnMoved as ProjectColumnMovedPayload
from githubkit.webhooks.models import PullRequestLabeled as PullRequestLabeledPayload
from githubkit.webhooks.models import ReleasePrereleased as ReleasePrereleasedPayload
from githubkit.webhooks.models import ReleaseUnpublished as ReleaseUnpublishedPayload
from githubkit.webhooks.models import RepositoryArchived as RepositoryArchivedPayload
from githubkit.webhooks.models import SponsorshipCreated as SponsorshipCreatedPayload
from githubkit.webhooks.models import CheckRunRerequested as CheckRunRerequestedPayload
from githubkit.webhooks.models import CheckSuiteCompleted as CheckSuiteCompletedPayload
from githubkit.webhooks.models import CheckSuiteRequested as CheckSuiteRequestedPayload
from githubkit.webhooks.models import DiscussionUnlabeled as DiscussionUnlabeledPayload
from githubkit.webhooks.models import InstallationCreated as InstallationCreatedPayload
from githubkit.webhooks.models import InstallationDeleted as InstallationDeletedPayload
from githubkit.webhooks.models import InstallationSuspend as InstallationSuspendPayload
from githubkit.webhooks.models import IssueCommentCreated as IssueCommentCreatedPayload
from githubkit.webhooks.models import IssueCommentDeleted as IssueCommentDeletedPayload
from githubkit.webhooks.models import OrganizationDeleted as OrganizationDeletedPayload
from githubkit.webhooks.models import OrganizationRenamed as OrganizationRenamedPayload
from githubkit.webhooks.models import ProjectColumnEdited as ProjectColumnEditedPayload
from githubkit.webhooks.models import PullRequestAssigned as PullRequestAssignedPayload
from githubkit.webhooks.models import PullRequestReopened as PullRequestReopenedPayload
from githubkit.webhooks.models import PullRequestUnlocked as PullRequestUnlockedPayload
from githubkit.webhooks.models import (
    CommitCommentCreated as CommitCommentCreatedPayload,
)
from githubkit.webhooks.models import (
    DiscussionUnanswered as DiscussionUnansweredPayload,
)
from githubkit.webhooks.models import (
    ProjectCardConverted as ProjectCardConvertedPayload,
)
from githubkit.webhooks.models import (
    ProjectColumnCreated as ProjectColumnCreatedPayload,
)
from githubkit.webhooks.models import (
    ProjectColumnDeleted as ProjectColumnDeletedPayload,
)
from githubkit.webhooks.models import (
    ProjectsV2ItemEdited as ProjectsV2ItemEditedPayload,
)
from githubkit.webhooks.models import (
    PullRequestUnlabeled as PullRequestUnlabeledPayload,
)
from githubkit.webhooks.models import (
    RepositoryPrivatized as RepositoryPrivatizedPayload,
)
from githubkit.webhooks.models import (
    RepositoryPublicized as RepositoryPublicizedPayload,
)
from githubkit.webhooks.models import (
    RepositoryUnarchived as RepositoryUnarchivedPayload,
)
from githubkit.webhooks.models import (
    SponsorshipCancelled as SponsorshipCancelledPayload,
)
from githubkit.webhooks.models import (
    WorkflowJobCompleted as WorkflowJobCompletedPayload,
)
from githubkit.webhooks.models import (
    WorkflowRunCompleted as WorkflowRunCompletedPayload,
)
from githubkit.webhooks.models import (
    WorkflowRunRequested as WorkflowRunRequestedPayload,
)
from githubkit.webhooks.models import (
    CheckSuiteRerequested as CheckSuiteRerequestedPayload,
)
from githubkit.webhooks.models import (
    DiscussionTransferred as DiscussionTransferredPayload,
)
from githubkit.webhooks.models import (
    InstallationUnsuspend as InstallationUnsuspendPayload,
)
from githubkit.webhooks.models import (
    ProjectsV2ItemCreated as ProjectsV2ItemCreatedPayload,
)
from githubkit.webhooks.models import (
    ProjectsV2ItemDeleted as ProjectsV2ItemDeletedPayload,
)
from githubkit.webhooks.models import (
    PullRequestUnassigned as PullRequestUnassignedPayload,
)
from githubkit.webhooks.models import (
    RepositoryImportEvent as RepositoryImportEventPayload,
)
from githubkit.webhooks.models import (
    RepositoryTransferred as RepositoryTransferredPayload,
)
from githubkit.webhooks.models import (
    TeamAddedToRepository as TeamAddedToRepositoryPayload,
)
from githubkit.webhooks.models import (
    WorkflowDispatchEvent as WorkflowDispatchEventPayload,
)
from githubkit.webhooks.models import (
    WorkflowJobInProgress as WorkflowJobInProgressPayload,
)
from githubkit.webhooks.models import (
    CodeScanningAlertFixed as CodeScanningAlertFixedPayload,
)
from githubkit.webhooks.models import (
    ProjectsV2ItemArchived as ProjectsV2ItemArchivedPayload,
)
from githubkit.webhooks.models import (
    ProjectsV2ItemRestored as ProjectsV2ItemRestoredPayload,
)
from githubkit.webhooks.models import (
    PullRequestSynchronize as PullRequestSynchronizePayload,
)
from githubkit.webhooks.models import (
    SponsorshipTierChanged as SponsorshipTierChangedPayload,
)
from githubkit.webhooks.models import (
    CheckRunRequestedAction as CheckRunRequestedActionPayload,
)
from githubkit.webhooks.models import (
    DeploymentStatusCreated as DeploymentStatusCreatedPayload,
)
from githubkit.webhooks.models import (
    DiscussionCommentEdited as DiscussionCommentEditedPayload,
)
from githubkit.webhooks.models import (
    OrganizationMemberAdded as OrganizationMemberAddedPayload,
)
from githubkit.webhooks.models import (
    ProjectsV2ItemConverted as ProjectsV2ItemConvertedPayload,
)
from githubkit.webhooks.models import (
    ProjectsV2ItemReordered as ProjectsV2ItemReorderedPayload,
)
from githubkit.webhooks.models import (
    PullRequestReviewEdited as PullRequestReviewEditedPayload,
)
from githubkit.webhooks.models import (
    RepositoryDispatchEvent as RepositoryDispatchEventPayload,
)
from githubkit.webhooks.models import (
    SecurityAdvisoryUpdated as SecurityAdvisoryUpdatedPayload,
)
from githubkit.webhooks.models import (
    CodeScanningAlertCreated as CodeScanningAlertCreatedPayload,
)
from githubkit.webhooks.models import (
    DiscussionCommentCreated as DiscussionCommentCreatedPayload,
)
from githubkit.webhooks.models import (
    DiscussionCommentDeleted as DiscussionCommentDeletedPayload,
)
from githubkit.webhooks.models import (
    CodeScanningAlertReopened as CodeScanningAlertReopenedPayload,
)
from githubkit.webhooks.models import (
    DiscussionCategoryChanged as DiscussionCategoryChangedPayload,
)
from githubkit.webhooks.models import (
    OrganizationMemberInvited as OrganizationMemberInvitedPayload,
)
from githubkit.webhooks.models import (
    OrganizationMemberRemoved as OrganizationMemberRemovedPayload,
)
from githubkit.webhooks.models import (
    PullRequestReadyForReview as PullRequestReadyForReviewPayload,
)
from githubkit.webhooks.models import (
    SecurityAdvisoryPerformed as SecurityAdvisoryPerformedPayload,
)
from githubkit.webhooks.models import (
    SecurityAdvisoryPublished as SecurityAdvisoryPublishedPayload,
)
from githubkit.webhooks.models import (
    SecurityAdvisoryWithdrawn as SecurityAdvisoryWithdrawnPayload,
)
from githubkit.webhooks.models import (
    TeamRemovedFromRepository as TeamRemovedFromRepositoryPayload,
)
from githubkit.webhooks.models import (
    BranchProtectionRuleEdited as BranchProtectionRuleEditedPayload,
)
from githubkit.webhooks.models import (
    MarketplacePurchaseChanged as MarketplacePurchaseChangedPayload,
)
from githubkit.webhooks.models import (
    PullRequestReviewDismissed as PullRequestReviewDismissedPayload,
)
from githubkit.webhooks.models import (
    PullRequestReviewSubmitted as PullRequestReviewSubmittedPayload,
)
from githubkit.webhooks.models import (
    SecretScanningAlertCreated as SecretScanningAlertCreatedPayload,
)
from githubkit.webhooks.models import (
    BranchProtectionRuleCreated as BranchProtectionRuleCreatedPayload,
)
from githubkit.webhooks.models import (
    BranchProtectionRuleDeleted as BranchProtectionRuleDeletedPayload,
)
from githubkit.webhooks.models import (
    PullRequestAutoMergeEnabled as PullRequestAutoMergeEnabledPayload,
)
from githubkit.webhooks.models import (
    PullRequestConvertedToDraft as PullRequestConvertedToDraftPayload,
)
from githubkit.webhooks.models import (
    SecretScanningAlertReopened as SecretScanningAlertReopenedPayload,
)
from githubkit.webhooks.models import (
    SecretScanningAlertResolved as SecretScanningAlertResolvedPayload,
)
from githubkit.webhooks.models import (
    MarketplacePurchaseCancelled as MarketplacePurchaseCancelledPayload,
)
from githubkit.webhooks.models import (
    MarketplacePurchasePurchased as MarketplacePurchasePurchasedPayload,
)
from githubkit.webhooks.models import (
    PullRequestAutoMergeDisabled as PullRequestAutoMergeDisabledPayload,
)
from githubkit.webhooks.models import (
    SponsorshipPendingTierChange as SponsorshipPendingTierChangePayload,
)
from githubkit.webhooks.models import (
    CodeScanningAlertClosedByUser as CodeScanningAlertClosedByUserPayload,
)
from githubkit.webhooks.models import (
    GithubAppAuthorizationRevoked as GithubAppAuthorizationRevokedPayload,
)
from githubkit.webhooks.models import (
    InstallationRepositoriesAdded as InstallationRepositoriesAddedPayload,
)
from githubkit.webhooks.models import (
    PullRequestReviewRequestedOneof0,
    PullRequestReviewRequestedOneof1,
)
from githubkit.webhooks.models import (
    PullRequestReviewCommentEdited as PullRequestReviewCommentEditedPayload,
)
from githubkit.webhooks.models import (
    SponsorshipPendingCancellation as SponsorshipPendingCancellationPayload,
)
from githubkit.webhooks.models import (
    CodeScanningAlertReopenedByUser as CodeScanningAlertReopenedByUserPayload,
)
from githubkit.webhooks.models import (
    InstallationRepositoriesRemoved as InstallationRepositoriesRemovedPayload,
)
from githubkit.webhooks.models import (
    PullRequestReviewCommentCreated as PullRequestReviewCommentCreatedPayload,
)
from githubkit.webhooks.models import (
    PullRequestReviewCommentDeleted as PullRequestReviewCommentDeletedPayload,
)
from githubkit.webhooks.models import (
    PullRequestReviewThreadResolved as PullRequestReviewThreadResolvedPayload,
)
from githubkit.webhooks.models import (
    MarketplacePurchasePendingChange as MarketplacePurchasePendingChangePayload,
)
from githubkit.webhooks.models import (
    CodeScanningAlertAppearedInBranch as CodeScanningAlertAppearedInBranchPayload,
)
from githubkit.webhooks.models import (
    PullRequestReviewThreadUnresolved as PullRequestReviewThreadUnresolvedPayload,
)
from githubkit.webhooks.models import (
    InstallationNewPermissionsAccepted as InstallationNewPermissionsAcceptedPayload,
)
from githubkit.webhooks.models import (
    RepositoryVulnerabilityAlertCreate as RepositoryVulnerabilityAlertCreatePayload,
)
from githubkit.webhooks.models import (
    RepositoryVulnerabilityAlertReopen as RepositoryVulnerabilityAlertReopenPayload,
)
from githubkit.webhooks.models import (
    PullRequestReviewRequestRemovedOneof0,
    PullRequestReviewRequestRemovedOneof1,
)
from githubkit.webhooks.models import (
    RepositoryVulnerabilityAlertDismiss as RepositoryVulnerabilityAlertDismissPayload,
)
from githubkit.webhooks.models import (
    RepositoryVulnerabilityAlertResolve as RepositoryVulnerabilityAlertResolvePayload,
)
from githubkit.webhooks.models import (
    MarketplacePurchasePendingChangeCancelled as MarketplacePurchasePendingChangeCancelledPayload,
)

from nonebot.adapters import Event as BaseEvent

from .message import Message
from .utils import get_attr_or_item


class Event(BaseEvent):
    id: str
    name: str
    payload: Dict[str, Any]

    to_me: bool = False

    @overrides(BaseEvent)
    def get_type(self) -> str:
        return "notice"

    @overrides(BaseEvent)
    def get_event_name(self) -> str:
        return self.name + (
            f".{action}" if (action := get_attr_or_item(self.payload, "action")) else ""
        )

    @overrides(BaseEvent)
    def get_event_description(self) -> str:
        return escape_tag(
            f"{self.__class__.__name__} "
            + (
                f"from sender {sender.login}"
                if (sender := get_attr_or_item(self.payload, "sender"))
                else ""
            )
            + (
                f"in repository {repo.full_name}"
                if (repo := get_attr_or_item(self.payload, "repository"))
                else ""
            )
        )

    @overrides(BaseEvent)
    def get_message(self) -> Message:
        raise ValueError("Event has no message!")

    @overrides(BaseEvent)
    def get_user_id(self) -> str:
        if sender := get_attr_or_item(self.payload, "sender"):
            return sender.login
        raise ValueError("Event has no context!")

    @overrides(BaseEvent)
    def get_session_id(self) -> str:
        return self.get_user_id()

    @overrides(BaseEvent)
    def is_tome(self) -> bool:
        return self.to_me


class CreateEvent(Event):
    payload: CreateEventPayload


class DeleteEvent(Event):
    payload: DeleteEventPayload


class ForkEvent(Event):
    payload: ForkEventPayload


class GollumEvent(Event):
    payload: GollumEventPayload


class PageBuildEvent(Event):
    payload: PageBuildEventPayload


class PingEvent(Event):
    payload: PingEventPayload


class PublicEvent(Event):
    payload: PublicEventPayload


class PushEvent(Event):
    payload: PushEventPayload


class RepositoryDispatchEvent(Event):
    payload: RepositoryDispatchEventPayload


class RepositoryImportEvent(Event):
    payload: RepositoryImportEventPayload


class StatusEvent(Event):
    payload: StatusEventPayload


class TeamAddEvent(Event):
    payload: TeamAddEventPayload


class WorkflowDispatchEvent(Event):
    payload: WorkflowDispatchEventPayload


class BranchProtectionRuleCreated(Event):
    payload: BranchProtectionRuleCreatedPayload


class BranchProtectionRuleDeleted(Event):
    payload: BranchProtectionRuleDeletedPayload


class BranchProtectionRuleEdited(Event):
    payload: BranchProtectionRuleEditedPayload


class CheckRunCompleted(Event):
    payload: CheckRunCompletedPayload


class CheckRunCreated(Event):
    payload: CheckRunCreatedPayload


class CheckRunRequestedAction(Event):
    payload: CheckRunRequestedActionPayload


class CheckRunRerequested(Event):
    payload: CheckRunRerequestedPayload


class CheckSuiteCompleted(Event):
    payload: CheckSuiteCompletedPayload


class CheckSuiteRequested(Event):
    payload: CheckSuiteRequestedPayload


class CheckSuiteRerequested(Event):
    payload: CheckSuiteRerequestedPayload


class CodeScanningAlertAppearedInBranch(Event):
    payload: CodeScanningAlertAppearedInBranchPayload


class CodeScanningAlertClosedByUser(Event):
    payload: CodeScanningAlertClosedByUserPayload


class CodeScanningAlertCreated(Event):
    payload: CodeScanningAlertCreatedPayload


class CodeScanningAlertFixed(Event):
    payload: CodeScanningAlertFixedPayload


class CodeScanningAlertReopened(Event):
    payload: CodeScanningAlertReopenedPayload


class CodeScanningAlertReopenedByUser(Event):
    payload: CodeScanningAlertReopenedByUserPayload


class CommitCommentCreated(Event):
    payload: CommitCommentCreatedPayload

    @overrides(Event)
    def get_type(self) -> str:
        return "message"

    @cached_property
    def _message(self):
        return Message(self.payload.comment.body)

    @overrides(Event)
    def get_message(self):
        return self._message

    class Config:
        keep_untouched = (cached_property,)


class DeployKeyCreated(Event):
    payload: DeployKeyCreatedPayload


class DeployKeyDeleted(Event):
    payload: DeployKeyDeletedPayload


class DeploymentCreated(Event):
    payload: DeploymentCreatedPayload


class DeploymentStatusCreated(Event):
    payload: DeploymentStatusCreatedPayload


class DiscussionAnswered(Event):
    payload: DiscussionAnsweredPayload


class DiscussionCategoryChanged(Event):
    payload: DiscussionCategoryChangedPayload


class DiscussionCreated(Event):
    payload: DiscussionCreatedPayload


class DiscussionDeleted(Event):
    payload: DiscussionDeletedPayload


class DiscussionEdited(Event):
    payload: DiscussionEditedPayload


class DiscussionLabeled(Event):
    payload: DiscussionLabeledPayload


class DiscussionLocked(Event):
    payload: DiscussionLockedPayload


class DiscussionPinned(Event):
    payload: DiscussionPinnedPayload


class DiscussionTransferred(Event):
    payload: DiscussionTransferredPayload


class DiscussionUnanswered(Event):
    payload: DiscussionUnansweredPayload


class DiscussionUnlabeled(Event):
    payload: DiscussionUnlabeledPayload


class DiscussionUnlocked(Event):
    payload: DiscussionUnlockedPayload


class DiscussionUnpinned(Event):
    payload: DiscussionUnpinnedPayload


class DiscussionCommentCreated(Event):
    payload: DiscussionCommentCreatedPayload


class DiscussionCommentDeleted(Event):
    payload: DiscussionCommentDeletedPayload


class DiscussionCommentEdited(Event):
    payload: DiscussionCommentEditedPayload


class GithubAppAuthorizationRevoked(Event):
    payload: GithubAppAuthorizationRevokedPayload


class InstallationCreated(Event):
    payload: InstallationCreatedPayload


class InstallationDeleted(Event):
    payload: InstallationDeletedPayload


class InstallationNewPermissionsAccepted(Event):
    payload: InstallationNewPermissionsAcceptedPayload


class InstallationSuspend(Event):
    payload: InstallationSuspendPayload


class InstallationUnsuspend(Event):
    payload: InstallationUnsuspendPayload


class InstallationRepositoriesAdded(Event):
    payload: InstallationRepositoriesAddedPayload


class InstallationRepositoriesRemoved(Event):
    payload: InstallationRepositoriesRemovedPayload


class IssueCommentCreated(Event):
    payload: IssueCommentCreatedPayload

    @overrides(Event)
    def get_type(self) -> str:
        return "message"

    @cached_property
    def _message(self):
        return Message(self.payload.comment.body)

    @overrides(Event)
    def get_message(self):
        return self._message

    class Config:
        keep_untouched = (cached_property,)


class IssueCommentDeleted(Event):
    payload: IssueCommentDeletedPayload

    @cached_property
    def _message(self):
        return Message(self.payload.comment.body)

    @overrides(Event)
    def get_message(self):
        return self._message

    class Config:
        keep_untouched = (cached_property,)


class IssueCommentEdited(Event):
    payload: IssueCommentEditedPayload

    @cached_property
    def _message(self):
        return Message(self.payload.comment.body)

    @overrides(Event)
    def get_message(self):
        return self._message

    class Config:
        keep_untouched = (cached_property,)


class IssuesAssigned(Event):
    payload: IssuesAssignedPayload


class IssuesClosed(Event):
    payload: IssuesClosedPayload


class IssuesDeleted(Event):
    payload: IssuesDeletedPayload


class IssuesDemilestoned(Event):
    payload: IssuesDemilestonedPayload


class IssuesEdited(Event):
    payload: IssuesEditedPayload


class IssuesLabeled(Event):
    payload: IssuesLabeledPayload


class IssuesLocked(Event):
    payload: IssuesLockedPayload


class IssuesMilestoned(Event):
    payload: IssuesMilestonedPayload


class IssuesOpened(Event):
    payload: IssuesOpenedPayload


class IssuesPinned(Event):
    payload: IssuesPinnedPayload


class IssuesReopened(Event):
    payload: IssuesReopenedPayload


class IssuesTransferred(Event):
    payload: IssuesTransferredPayload


class IssuesUnassigned(Event):
    payload: IssuesUnassignedPayload


class IssuesUnlabeled(Event):
    payload: IssuesUnlabeledPayload


class IssuesUnlocked(Event):
    payload: IssuesUnlockedPayload


class IssuesUnpinned(Event):
    payload: IssuesUnpinnedPayload


class LabelCreated(Event):
    payload: LabelCreatedPayload


class LabelDeleted(Event):
    payload: LabelDeletedPayload


class LabelEdited(Event):
    payload: LabelEditedPayload


class MarketplacePurchaseCancelled(Event):
    payload: MarketplacePurchaseCancelledPayload


class MarketplacePurchaseChanged(Event):
    payload: MarketplacePurchaseChangedPayload


class MarketplacePurchasePendingChange(Event):
    payload: MarketplacePurchasePendingChangePayload


class MarketplacePurchasePendingChangeCancelled(Event):
    payload: MarketplacePurchasePendingChangeCancelledPayload


class MarketplacePurchasePurchased(Event):
    payload: MarketplacePurchasePurchasedPayload


class MemberAdded(Event):
    payload: MemberAddedPayload


class MemberEdited(Event):
    payload: MemberEditedPayload


class MemberRemoved(Event):
    payload: MemberRemovedPayload


class MembershipAdded(Event):
    payload: MembershipAddedPayload


class MembershipRemoved(Event):
    payload: MembershipRemovedPayload


class MetaDeleted(Event):
    payload: MetaDeletedPayload


class MilestoneClosed(Event):
    payload: MilestoneClosedPayload


class MilestoneCreated(Event):
    payload: MilestoneCreatedPayload


class MilestoneDeleted(Event):
    payload: MilestoneDeletedPayload


class MilestoneEdited(Event):
    payload: MilestoneEditedPayload


class MilestoneOpened(Event):
    payload: MilestoneOpenedPayload


class OrgBlockBlocked(Event):
    payload: OrgBlockBlockedPayload


class OrgBlockUnblocked(Event):
    payload: OrgBlockUnblockedPayload


class OrganizationDeleted(Event):
    payload: OrganizationDeletedPayload


class OrganizationMemberAdded(Event):
    payload: OrganizationMemberAddedPayload


class OrganizationMemberInvited(Event):
    payload: OrganizationMemberInvitedPayload


class OrganizationMemberRemoved(Event):
    payload: OrganizationMemberRemovedPayload


class OrganizationRenamed(Event):
    payload: OrganizationRenamedPayload


class PackagePublished(Event):
    payload: PackagePublishedPayload


class PackageUpdated(Event):
    payload: PackageUpdatedPayload


class ProjectClosed(Event):
    payload: ProjectClosedPayload


class ProjectCreated(Event):
    payload: ProjectCreatedPayload


class ProjectDeleted(Event):
    payload: ProjectDeletedPayload


class ProjectEdited(Event):
    payload: ProjectEditedPayload


class ProjectReopened(Event):
    payload: ProjectReopenedPayload


class ProjectCardConverted(Event):
    payload: ProjectCardConvertedPayload


class ProjectCardCreated(Event):
    payload: ProjectCardCreatedPayload


class ProjectCardDeleted(Event):
    payload: ProjectCardDeletedPayload


class ProjectCardEdited(Event):
    payload: ProjectCardEditedPayload


class ProjectCardMoved(Event):
    payload: ProjectCardMovedPayload


class ProjectColumnCreated(Event):
    payload: ProjectColumnCreatedPayload


class ProjectColumnDeleted(Event):
    payload: ProjectColumnDeletedPayload


class ProjectColumnEdited(Event):
    payload: ProjectColumnEditedPayload


class ProjectColumnMoved(Event):
    payload: ProjectColumnMovedPayload


class ProjectsV2ItemArchived(Event):
    payload: ProjectsV2ItemArchivedPayload


class ProjectsV2ItemConverted(Event):
    payload: ProjectsV2ItemConvertedPayload


class ProjectsV2ItemCreated(Event):
    payload: ProjectsV2ItemCreatedPayload


class ProjectsV2ItemDeleted(Event):
    payload: ProjectsV2ItemDeletedPayload


class ProjectsV2ItemEdited(Event):
    payload: ProjectsV2ItemEditedPayload


class ProjectsV2ItemReordered(Event):
    payload: ProjectsV2ItemReorderedPayload


class ProjectsV2ItemRestored(Event):
    payload: ProjectsV2ItemRestoredPayload


class PullRequestAssigned(Event):
    payload: PullRequestAssignedPayload


class PullRequestAutoMergeDisabled(Event):
    payload: PullRequestAutoMergeDisabledPayload


class PullRequestAutoMergeEnabled(Event):
    payload: PullRequestAutoMergeEnabledPayload


class PullRequestClosed(Event):
    payload: PullRequestClosedPayload


class PullRequestConvertedToDraft(Event):
    payload: PullRequestConvertedToDraftPayload


class PullRequestEdited(Event):
    payload: PullRequestEditedPayload


class PullRequestLabeled(Event):
    payload: PullRequestLabeledPayload


class PullRequestLocked(Event):
    payload: PullRequestLockedPayload


class PullRequestOpened(Event):
    payload: PullRequestOpenedPayload


class PullRequestReadyForReview(Event):
    payload: PullRequestReadyForReviewPayload


class PullRequestReopened(Event):
    payload: PullRequestReopenedPayload


class PullRequestReviewRequestRemoved(Event):
    payload: Union[
        PullRequestReviewRequestRemovedOneof0, PullRequestReviewRequestRemovedOneof1
    ]


class PullRequestReviewRequested(Event):
    payload: Union[PullRequestReviewRequestedOneof0, PullRequestReviewRequestedOneof1]


class PullRequestSynchronize(Event):
    payload: PullRequestSynchronizePayload


class PullRequestUnassigned(Event):
    payload: PullRequestUnassignedPayload


class PullRequestUnlabeled(Event):
    payload: PullRequestUnlabeledPayload


class PullRequestUnlocked(Event):
    payload: PullRequestUnlockedPayload


class PullRequestReviewDismissed(Event):
    payload: PullRequestReviewDismissedPayload


class PullRequestReviewEdited(Event):
    payload: PullRequestReviewEditedPayload


class PullRequestReviewSubmitted(Event):
    payload: PullRequestReviewSubmittedPayload


class PullRequestReviewCommentCreated(Event):
    payload: PullRequestReviewCommentCreatedPayload

    @overrides(Event)
    def get_type(self) -> str:
        return "message"

    @cached_property
    def _message(self):
        return Message(self.payload.comment.body)

    @overrides(Event)
    def get_message(self):
        return self._message

    class Config:
        keep_untouched = (cached_property,)


class PullRequestReviewCommentDeleted(Event):
    payload: PullRequestReviewCommentDeletedPayload

    @cached_property
    def _message(self):
        return Message(self.payload.comment.body)

    @overrides(Event)
    def get_message(self):
        return self._message

    class Config:
        keep_untouched = (cached_property,)


class PullRequestReviewCommentEdited(Event):
    payload: PullRequestReviewCommentEditedPayload

    @cached_property
    def _message(self):
        return Message(self.payload.comment.body)

    @overrides(Event)
    def get_message(self):
        return self._message

    class Config:
        keep_untouched = (cached_property,)


class PullRequestReviewThreadResolved(Event):
    payload: PullRequestReviewThreadResolvedPayload


class PullRequestReviewThreadUnresolved(Event):
    payload: PullRequestReviewThreadUnresolvedPayload


class ReleaseCreated(Event):
    payload: ReleaseCreatedPayload


class ReleaseDeleted(Event):
    payload: ReleaseDeletedPayload


class ReleaseEdited(Event):
    payload: ReleaseEditedPayload


class ReleasePrereleased(Event):
    payload: ReleasePrereleasedPayload


class ReleasePublished(Event):
    payload: ReleasePublishedPayload


class ReleaseReleased(Event):
    payload: ReleaseReleasedPayload


class ReleaseUnpublished(Event):
    payload: ReleaseUnpublishedPayload


class RepositoryArchived(Event):
    payload: RepositoryArchivedPayload


class RepositoryCreated(Event):
    payload: RepositoryCreatedPayload


class RepositoryDeleted(Event):
    payload: RepositoryDeletedPayload


class RepositoryEdited(Event):
    payload: RepositoryEditedPayload


class RepositoryPrivatized(Event):
    payload: RepositoryPrivatizedPayload


class RepositoryPublicized(Event):
    payload: RepositoryPublicizedPayload


class RepositoryRenamed(Event):
    payload: RepositoryRenamedPayload


class RepositoryTransferred(Event):
    payload: RepositoryTransferredPayload


class RepositoryUnarchived(Event):
    payload: RepositoryUnarchivedPayload


class RepositoryVulnerabilityAlertCreate(Event):
    payload: RepositoryVulnerabilityAlertCreatePayload


class RepositoryVulnerabilityAlertDismiss(Event):
    payload: RepositoryVulnerabilityAlertDismissPayload


class RepositoryVulnerabilityAlertReopen(Event):
    payload: RepositoryVulnerabilityAlertReopenPayload


class RepositoryVulnerabilityAlertResolve(Event):
    payload: RepositoryVulnerabilityAlertResolvePayload


class SecretScanningAlertCreated(Event):
    payload: SecretScanningAlertCreatedPayload


class SecretScanningAlertReopened(Event):
    payload: SecretScanningAlertReopenedPayload


class SecretScanningAlertResolved(Event):
    payload: SecretScanningAlertResolvedPayload


class SecurityAdvisoryPerformed(Event):
    payload: SecurityAdvisoryPerformedPayload


class SecurityAdvisoryPublished(Event):
    payload: SecurityAdvisoryPublishedPayload


class SecurityAdvisoryUpdated(Event):
    payload: SecurityAdvisoryUpdatedPayload


class SecurityAdvisoryWithdrawn(Event):
    payload: SecurityAdvisoryWithdrawnPayload


class SponsorshipCancelled(Event):
    payload: SponsorshipCancelledPayload


class SponsorshipCreated(Event):
    payload: SponsorshipCreatedPayload


class SponsorshipEdited(Event):
    payload: SponsorshipEditedPayload


class SponsorshipPendingCancellation(Event):
    payload: SponsorshipPendingCancellationPayload


class SponsorshipPendingTierChange(Event):
    payload: SponsorshipPendingTierChangePayload


class SponsorshipTierChanged(Event):
    payload: SponsorshipTierChangedPayload


class StarCreated(Event):
    payload: StarCreatedPayload


class StarDeleted(Event):
    payload: StarDeletedPayload


class TeamAddedToRepository(Event):
    payload: TeamAddedToRepositoryPayload


class TeamCreated(Event):
    payload: TeamCreatedPayload


class TeamDeleted(Event):
    payload: TeamDeletedPayload


class TeamEdited(Event):
    payload: TeamEditedPayload


class TeamRemovedFromRepository(Event):
    payload: TeamRemovedFromRepositoryPayload


class WatchStarted(Event):
    payload: WatchStartedPayload


class WorkflowJobCompleted(Event):
    payload: WorkflowJobCompletedPayload


class WorkflowJobInProgress(Event):
    payload: WorkflowJobInProgressPayload


class WorkflowJobQueued(Event):
    payload: WorkflowJobQueuedPayload


class WorkflowRunCompleted(Event):
    payload: WorkflowRunCompletedPayload


class WorkflowRunRequested(Event):
    payload: WorkflowRunRequestedPayload


events = {
    "create": CreateEvent,
    "delete": DeleteEvent,
    "fork": ForkEvent,
    "gollum": GollumEvent,
    "page_build": PageBuildEvent,
    "ping": PingEvent,
    "public": PublicEvent,
    "push": PushEvent,
    "repository_dispatch": RepositoryDispatchEvent,
    "repository_import": RepositoryImportEvent,
    "status": StatusEvent,
    "team_add": TeamAddEvent,
    "workflow_dispatch": WorkflowDispatchEvent,
    "branch_protection_rule": {
        "created": BranchProtectionRuleCreated,
        "deleted": BranchProtectionRuleDeleted,
        "edited": BranchProtectionRuleEdited,
    },
    "check_run": {
        "completed": CheckRunCompleted,
        "created": CheckRunCreated,
        "requested_action": CheckRunRequestedAction,
        "rerequested": CheckRunRerequested,
    },
    "check_suite": {
        "completed": CheckSuiteCompleted,
        "requested": CheckSuiteRequested,
        "rerequested": CheckSuiteRerequested,
    },
    "code_scanning_alert": {
        "appeared_in_branch": CodeScanningAlertAppearedInBranch,
        "closed_by_user": CodeScanningAlertClosedByUser,
        "created": CodeScanningAlertCreated,
        "fixed": CodeScanningAlertFixed,
        "reopened": CodeScanningAlertReopened,
        "reopened_by_user": CodeScanningAlertReopenedByUser,
    },
    "commit_comment": {
        "created": CommitCommentCreated,
    },
    "deploy_key": {
        "created": DeployKeyCreated,
        "deleted": DeployKeyDeleted,
    },
    "deployment": {
        "created": DeploymentCreated,
    },
    "deployment_status": {
        "created": DeploymentStatusCreated,
    },
    "discussion": {
        "answered": DiscussionAnswered,
        "category_changed": DiscussionCategoryChanged,
        "created": DiscussionCreated,
        "deleted": DiscussionDeleted,
        "edited": DiscussionEdited,
        "labeled": DiscussionLabeled,
        "locked": DiscussionLocked,
        "pinned": DiscussionPinned,
        "transferred": DiscussionTransferred,
        "unanswered": DiscussionUnanswered,
        "unlabeled": DiscussionUnlabeled,
        "unlocked": DiscussionUnlocked,
        "unpinned": DiscussionUnpinned,
    },
    "discussion_comment": {
        "created": DiscussionCommentCreated,
        "deleted": DiscussionCommentDeleted,
        "edited": DiscussionCommentEdited,
    },
    "github_app_authorization": {
        "revoked": GithubAppAuthorizationRevoked,
    },
    "installation": {
        "created": InstallationCreated,
        "deleted": InstallationDeleted,
        "new_permissions_accepted": InstallationNewPermissionsAccepted,
        "suspend": InstallationSuspend,
        "unsuspend": InstallationUnsuspend,
    },
    "installation_repositories": {
        "added": InstallationRepositoriesAdded,
        "removed": InstallationRepositoriesRemoved,
    },
    "issue_comment": {
        "created": IssueCommentCreated,
        "deleted": IssueCommentDeleted,
        "edited": IssueCommentEdited,
    },
    "issues": {
        "assigned": IssuesAssigned,
        "closed": IssuesClosed,
        "deleted": IssuesDeleted,
        "demilestoned": IssuesDemilestoned,
        "edited": IssuesEdited,
        "labeled": IssuesLabeled,
        "locked": IssuesLocked,
        "milestoned": IssuesMilestoned,
        "opened": IssuesOpened,
        "pinned": IssuesPinned,
        "reopened": IssuesReopened,
        "transferred": IssuesTransferred,
        "unassigned": IssuesUnassigned,
        "unlabeled": IssuesUnlabeled,
        "unlocked": IssuesUnlocked,
        "unpinned": IssuesUnpinned,
    },
    "label": {
        "created": LabelCreated,
        "deleted": LabelDeleted,
        "edited": LabelEdited,
    },
    "marketplace_purchase": {
        "cancelled": MarketplacePurchaseCancelled,
        "changed": MarketplacePurchaseChanged,
        "pending_change": MarketplacePurchasePendingChange,
        "pending_change_cancelled": MarketplacePurchasePendingChangeCancelled,
        "purchased": MarketplacePurchasePurchased,
    },
    "member": {
        "added": MemberAdded,
        "edited": MemberEdited,
        "removed": MemberRemoved,
    },
    "membership": {
        "added": MembershipAdded,
        "removed": MembershipRemoved,
    },
    "meta": {
        "deleted": MetaDeleted,
    },
    "milestone": {
        "closed": MilestoneClosed,
        "created": MilestoneCreated,
        "deleted": MilestoneDeleted,
        "edited": MilestoneEdited,
        "opened": MilestoneOpened,
    },
    "org_block": {
        "blocked": OrgBlockBlocked,
        "unblocked": OrgBlockUnblocked,
    },
    "organization": {
        "deleted": OrganizationDeleted,
        "member_added": OrganizationMemberAdded,
        "member_invited": OrganizationMemberInvited,
        "member_removed": OrganizationMemberRemoved,
        "renamed": OrganizationRenamed,
    },
    "package": {
        "published": PackagePublished,
        "updated": PackageUpdated,
    },
    "project": {
        "closed": ProjectClosed,
        "created": ProjectCreated,
        "deleted": ProjectDeleted,
        "edited": ProjectEdited,
        "reopened": ProjectReopened,
    },
    "project_card": {
        "converted": ProjectCardConverted,
        "created": ProjectCardCreated,
        "deleted": ProjectCardDeleted,
        "edited": ProjectCardEdited,
        "moved": ProjectCardMoved,
    },
    "project_column": {
        "created": ProjectColumnCreated,
        "deleted": ProjectColumnDeleted,
        "edited": ProjectColumnEdited,
        "moved": ProjectColumnMoved,
    },
    "projects_v2_item": {
        "archived": ProjectsV2ItemArchived,
        "converted": ProjectsV2ItemConverted,
        "created": ProjectsV2ItemCreated,
        "deleted": ProjectsV2ItemDeleted,
        "edited": ProjectsV2ItemEdited,
        "reordered": ProjectsV2ItemReordered,
        "restored": ProjectsV2ItemRestored,
    },
    "pull_request": {
        "assigned": PullRequestAssigned,
        "auto_merge_disabled": PullRequestAutoMergeDisabled,
        "auto_merge_enabled": PullRequestAutoMergeEnabled,
        "closed": PullRequestClosed,
        "converted_to_draft": PullRequestConvertedToDraft,
        "edited": PullRequestEdited,
        "labeled": PullRequestLabeled,
        "locked": PullRequestLocked,
        "opened": PullRequestOpened,
        "ready_for_review": PullRequestReadyForReview,
        "reopened": PullRequestReopened,
        "review_request_removed": PullRequestReviewRequestRemoved,
        "review_requested": PullRequestReviewRequested,
        "synchronize": PullRequestSynchronize,
        "unassigned": PullRequestUnassigned,
        "unlabeled": PullRequestUnlabeled,
        "unlocked": PullRequestUnlocked,
    },
    "pull_request_review": {
        "dismissed": PullRequestReviewDismissed,
        "edited": PullRequestReviewEdited,
        "submitted": PullRequestReviewSubmitted,
    },
    "pull_request_review_comment": {
        "created": PullRequestReviewCommentCreated,
        "deleted": PullRequestReviewCommentDeleted,
        "edited": PullRequestReviewCommentEdited,
    },
    "pull_request_review_thread": {
        "resolved": PullRequestReviewThreadResolved,
        "unresolved": PullRequestReviewThreadUnresolved,
    },
    "release": {
        "created": ReleaseCreated,
        "deleted": ReleaseDeleted,
        "edited": ReleaseEdited,
        "prereleased": ReleasePrereleased,
        "published": ReleasePublished,
        "released": ReleaseReleased,
        "unpublished": ReleaseUnpublished,
    },
    "repository": {
        "archived": RepositoryArchived,
        "created": RepositoryCreated,
        "deleted": RepositoryDeleted,
        "edited": RepositoryEdited,
        "privatized": RepositoryPrivatized,
        "publicized": RepositoryPublicized,
        "renamed": RepositoryRenamed,
        "transferred": RepositoryTransferred,
        "unarchived": RepositoryUnarchived,
    },
    "repository_vulnerability_alert": {
        "create": RepositoryVulnerabilityAlertCreate,
        "dismiss": RepositoryVulnerabilityAlertDismiss,
        "reopen": RepositoryVulnerabilityAlertReopen,
        "resolve": RepositoryVulnerabilityAlertResolve,
    },
    "secret_scanning_alert": {
        "created": SecretScanningAlertCreated,
        "reopened": SecretScanningAlertReopened,
        "resolved": SecretScanningAlertResolved,
    },
    "security_advisory": {
        "performed": SecurityAdvisoryPerformed,
        "published": SecurityAdvisoryPublished,
        "updated": SecurityAdvisoryUpdated,
        "withdrawn": SecurityAdvisoryWithdrawn,
    },
    "sponsorship": {
        "cancelled": SponsorshipCancelled,
        "created": SponsorshipCreated,
        "edited": SponsorshipEdited,
        "pending_cancellation": SponsorshipPendingCancellation,
        "pending_tier_change": SponsorshipPendingTierChange,
        "tier_changed": SponsorshipTierChanged,
    },
    "star": {
        "created": StarCreated,
        "deleted": StarDeleted,
    },
    "team": {
        "added_to_repository": TeamAddedToRepository,
        "created": TeamCreated,
        "deleted": TeamDeleted,
        "edited": TeamEdited,
        "removed_from_repository": TeamRemovedFromRepository,
    },
    "watch": {
        "started": WatchStarted,
    },
    "workflow_job": {
        "completed": WorkflowJobCompleted,
        "in_progress": WorkflowJobInProgress,
        "queued": WorkflowJobQueued,
    },
    "workflow_run": {
        "completed": WorkflowRunCompleted,
        "requested": WorkflowRunRequested,
    },
}
