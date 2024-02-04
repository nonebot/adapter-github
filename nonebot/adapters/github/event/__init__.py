from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .fork import Fork as Fork
    from .ping import Ping as Ping
    from .push import Push as Push
    from ._base import Event as Event
    from ._types import events as events
    from .create import Create as Create
    from .delete import Delete as Delete
    from .gollum import Gollum as Gollum
    from .public import Public as Public
    from .status import Status as Status
    from .team_add import TeamAdd as TeamAdd
    from .meta import MetaDeleted as MetaDeleted
    from .page_build import PageBuild as PageBuild
    from .watch import WatchStarted as WatchStarted
    from .team_edited import TeamEdited as TeamEdited
    from .label_edited import LabelEdited as LabelEdited
    from .member_added import MemberAdded as MemberAdded
    from .star_created import StarCreated as StarCreated
    from .star_deleted import StarDeleted as StarDeleted
    from .team_created import TeamCreated as TeamCreated
    from .team_deleted import TeamDeleted as TeamDeleted
    from .issues_closed import IssuesClosed as IssuesClosed
    from .issues_edited import IssuesEdited as IssuesEdited
    from .issues_locked import IssuesLocked as IssuesLocked
    from .issues_opened import IssuesOpened as IssuesOpened
    from .issues_pinned import IssuesPinned as IssuesPinned
    from .label_created import LabelCreated as LabelCreated
    from .label_deleted import LabelDeleted as LabelDeleted
    from .member_edited import MemberEdited as MemberEdited
    from .issues_deleted import IssuesDeleted as IssuesDeleted
    from .issues_labeled import IssuesLabeled as IssuesLabeled
    from .member_removed import MemberRemoved as MemberRemoved
    from .project_closed import ProjectClosed as ProjectClosed
    from .project_edited import ProjectEdited as ProjectEdited
    from .release_edited import ReleaseEdited as ReleaseEdited
    from .issues_assigned import IssuesAssigned as IssuesAssigned
    from .issues_reopened import IssuesReopened as IssuesReopened
    from .issues_unlocked import IssuesUnlocked as IssuesUnlocked
    from .issues_unpinned import IssuesUnpinned as IssuesUnpinned
    from .package_updated import PackageUpdated as PackageUpdated
    from .project_created import ProjectCreated as ProjectCreated
    from .project_deleted import ProjectDeleted as ProjectDeleted
    from .release_created import ReleaseCreated as ReleaseCreated
    from .release_deleted import ReleaseDeleted as ReleaseDeleted
    from .deployment import DeploymentCreated as DeploymentCreated
    from .issues_unlabeled import IssuesUnlabeled as IssuesUnlabeled
    from .membership_added import MembershipAdded as MembershipAdded
    from .milestone_closed import MilestoneClosed as MilestoneClosed
    from .milestone_edited import MilestoneEdited as MilestoneEdited
    from .milestone_opened import MilestoneOpened as MilestoneOpened
    from .project_reopened import ProjectReopened as ProjectReopened
    from .release_released import ReleaseReleased as ReleaseReleased
    from .check_run_created import CheckRunCreated as CheckRunCreated
    from .org_block_blocked import OrgBlockBlocked as OrgBlockBlocked
    from .discussion_closed import DiscussionClosed as DiscussionClosed
    from .discussion_edited import DiscussionEdited as DiscussionEdited
    from .discussion_locked import DiscussionLocked as DiscussionLocked
    from .discussion_pinned import DiscussionPinned as DiscussionPinned
    from .issues_milestoned import IssuesMilestoned as IssuesMilestoned
    from .issues_unassigned import IssuesUnassigned as IssuesUnassigned
    from .milestone_created import MilestoneCreated as MilestoneCreated
    from .milestone_deleted import MilestoneDeleted as MilestoneDeleted
    from .package_published import PackagePublished as PackagePublished
    from .release_published import ReleasePublished as ReleasePublished
    from .repository_edited import RepositoryEdited as RepositoryEdited
    from .repository_import import RepositoryImport as RepositoryImport
    from .workflow_dispatch import WorkflowDispatch as WorkflowDispatch
    from .deploy_key_created import DeployKeyCreated as DeployKeyCreated
    from .deploy_key_deleted import DeployKeyDeleted as DeployKeyDeleted
    from .project_card_moved import ProjectCardMoved as ProjectCardMoved
    from .discussion_created import DiscussionCreated as DiscussionCreated
    from .discussion_deleted import DiscussionDeleted as DiscussionDeleted
    from .discussion_labeled import DiscussionLabeled as DiscussionLabeled
    from .issues_transferred import IssuesTransferred as IssuesTransferred
    from .membership_removed import MembershipRemoved as MembershipRemoved
    from .repository_created import RepositoryCreated as RepositoryCreated
    from .repository_deleted import RepositoryDeleted as RepositoryDeleted
    from .repository_renamed import RepositoryRenamed as RepositoryRenamed
    from .sponsorship_edited import SponsorshipEdited as SponsorshipEdited
    from .check_run_completed import CheckRunCompleted as CheckRunCompleted
    from .org_block_unblocked import OrgBlockUnblocked as OrgBlockUnblocked
    from .project_card_edited import ProjectCardEdited as ProjectCardEdited
    from .pull_request_closed import PullRequestClosed as PullRequestClosed
    from .pull_request_edited import PullRequestEdited as PullRequestEdited
    from .pull_request_locked import PullRequestLocked as PullRequestLocked
    from .pull_request_opened import PullRequestOpened as PullRequestOpened
    from .workflow_job_queued import WorkflowJobQueued as WorkflowJobQueued
    from .commit_comment import CommitCommentCreated as CommitCommentCreated
    from .discussion_answered import DiscussionAnswered as DiscussionAnswered
    from .discussion_reopened import DiscussionReopened as DiscussionReopened
    from .discussion_unlocked import DiscussionUnlocked as DiscussionUnlocked
    from .discussion_unpinned import DiscussionUnpinned as DiscussionUnpinned
    from .issues_demilestoned import IssuesDemilestoned as IssuesDemilestoned
    from .release_prereleased import ReleasePrereleased as ReleasePrereleased
    from .release_unpublished import ReleaseUnpublished as ReleaseUnpublished
    from .repository_archived import RepositoryArchived as RepositoryArchived
    from .sponsorship_created import SponsorshipCreated as SponsorshipCreated
    from .issue_comment_edited import IssueCommentEdited as IssueCommentEdited
    from .project_card_created import ProjectCardCreated as ProjectCardCreated
    from .project_card_deleted import ProjectCardDeleted as ProjectCardDeleted
    from .project_column_moved import ProjectColumnMoved as ProjectColumnMoved
    from .pull_request_labeled import PullRequestLabeled as PullRequestLabeled
    from .workflow_job_waiting import WorkflowJobWaiting as WorkflowJobWaiting
    from .discussion_unlabeled import DiscussionUnlabeled as DiscussionUnlabeled
    from .installation_created import InstallationCreated as InstallationCreated
    from .installation_deleted import InstallationDeleted as InstallationDeleted
    from .installation_suspend import InstallationSuspend as InstallationSuspend
    from .organization_deleted import OrganizationDeleted as OrganizationDeleted
    from .organization_renamed import OrganizationRenamed as OrganizationRenamed
    from .check_run_rerequested import CheckRunRerequested as CheckRunRerequested
    from .check_suite_completed import CheckSuiteCompleted as CheckSuiteCompleted
    from .check_suite_requested import CheckSuiteRequested as CheckSuiteRequested
    from .issue_comment_created import IssueCommentCreated as IssueCommentCreated
    from .issue_comment_deleted import IssueCommentDeleted as IssueCommentDeleted
    from .merge_group_destroyed import MergeGroupDestroyed as MergeGroupDestroyed
    from .project_column_edited import ProjectColumnEdited as ProjectColumnEdited
    from .pull_request_assigned import PullRequestAssigned as PullRequestAssigned
    from .pull_request_dequeued import PullRequestDequeued as PullRequestDequeued
    from .pull_request_enqueued import PullRequestEnqueued as PullRequestEnqueued
    from .pull_request_reopened import PullRequestReopened as PullRequestReopened
    from .pull_request_unlocked import PullRequestUnlocked as PullRequestUnlocked
    from .security_and_analysis import SecurityAndAnalysis as SecurityAndAnalysis
    from .discussion_unanswered import DiscussionUnanswered as DiscussionUnanswered
    from .repository_privatized import RepositoryPrivatized as RepositoryPrivatized
    from .repository_publicized import RepositoryPublicized as RepositoryPublicized
    from .repository_unarchived import RepositoryUnarchived as RepositoryUnarchived
    from .sponsorship_cancelled import SponsorshipCancelled as SponsorshipCancelled
    from .dependabot_alert_fixed import DependabotAlertFixed as DependabotAlertFixed
    from .project_card_converted import ProjectCardConverted as ProjectCardConverted
    from .project_column_created import ProjectColumnCreated as ProjectColumnCreated
    from .project_column_deleted import ProjectColumnDeleted as ProjectColumnDeleted
    from .pull_request_unlabeled import PullRequestUnlabeled as PullRequestUnlabeled
    from .workflow_job_completed import WorkflowJobCompleted as WorkflowJobCompleted
    from .workflow_run_completed import WorkflowRunCompleted as WorkflowRunCompleted
    from .workflow_run_requested import WorkflowRunRequested as WorkflowRunRequested
    from .deployment_status import DeploymentStatusCreated as DeploymentStatusCreated
    from .projects_v2_item_edited import ProjectsV2ItemEdited as ProjectsV2ItemEdited
    from .discussion_transferred import DiscussionTransferred as DiscussionTransferred
    from .installation_unsuspend import InstallationUnsuspend as InstallationUnsuspend
    from .projects_v2_closed import ProjectsV2ProjectClosed as ProjectsV2ProjectClosed
    from .projects_v2_edited import ProjectsV2ProjectEdited as ProjectsV2ProjectEdited
    from .repository_transferred import RepositoryTransferred as RepositoryTransferred
    from .check_suite_rerequested import CheckSuiteRerequested as CheckSuiteRerequested
    from .custom_property_created import CustomPropertyCreated as CustomPropertyCreated
    from .custom_property_deleted import CustomPropertyDeleted as CustomPropertyDeleted
    from .custom_property_updated import CustomPropertyUpdated as CustomPropertyUpdated
    from .pull_request_milestoned import PullRequestMilestoned as PullRequestMilestoned
    from .pull_request_unassigned import PullRequestUnassigned as PullRequestUnassigned
    from .projects_v2_item_created import ProjectsV2ItemCreated as ProjectsV2ItemCreated
    from .projects_v2_item_deleted import ProjectsV2ItemDeleted as ProjectsV2ItemDeleted
    from .team_added_to_repository import TeamAddedToRepository as TeamAddedToRepository
    from .workflow_job_in_progress import WorkflowJobInProgress as WorkflowJobInProgress
    from .workflow_run_in_progress import WorkflowRunInProgress as WorkflowRunInProgress
    from .projects_v2_created import (
        ProjectsV2ProjectCreated as ProjectsV2ProjectCreated,
    )
    from .projects_v2_deleted import (
        ProjectsV2ProjectDeleted as ProjectsV2ProjectDeleted,
    )
    from .repository_dispatch import (
        RepositoryDispatchSample as RepositoryDispatchSample,
    )
    from .dependabot_alert_created import (
        DependabotAlertCreated as DependabotAlertCreated,
    )
    from .pull_request_synchronize import (
        PullRequestSynchronize as PullRequestSynchronize,
    )
    from .registry_package_updated import (
        RegistryPackageUpdated as RegistryPackageUpdated,
    )
    from .sponsorship_tier_changed import (
        SponsorshipTierChanged as SponsorshipTierChanged,
    )
    from .code_scanning_alert_fixed import (
        CodeScanningAlertFixed as CodeScanningAlertFixed,
    )
    from .installation_target import (
        InstallationTargetRenamed as InstallationTargetRenamed,
    )
    from .projects_v2_item_archived import (
        ProjectsV2ItemArchived as ProjectsV2ItemArchived,
    )
    from .projects_v2_item_restored import (
        ProjectsV2ItemRestored as ProjectsV2ItemRestored,
    )
    from .projects_v2_reopened import (
        ProjectsV2ProjectReopened as ProjectsV2ProjectReopened,
    )
    from .dependabot_alert_reopened import (
        DependabotAlertReopened as DependabotAlertReopened,
    )
    from .discussion_comment_edited import (
        DiscussionCommentEdited as DiscussionCommentEdited,
    )
    from .organization_member_added import (
        OrganizationMemberAdded as OrganizationMemberAdded,
    )
    from .pull_request_demilestoned import (
        PullRequestDemilestoned as PullRequestDemilestoned,
    )
    from .repository_ruleset_edited import (
        RepositoryRulesetEdited as RepositoryRulesetEdited,
    )
    from .security_advisory_updated import (
        SecurityAdvisoryUpdated as SecurityAdvisoryUpdated,
    )
    from .check_run_requested_action import (
        CheckRunRequestedAction as CheckRunRequestedAction,
    )
    from .projects_v2_item_converted import (
        ProjectsV2ItemConverted as ProjectsV2ItemConverted,
    )
    from .projects_v2_item_reordered import (
        ProjectsV2ItemReordered as ProjectsV2ItemReordered,
    )
    from .pull_request_review_edited import (
        PullRequestReviewEdited as PullRequestReviewEdited,
    )
    from .dependabot_alert_dismissed import (
        DependabotAlertDismissed as DependabotAlertDismissed,
    )
    from .deployment_review_approved import (
        DeploymentReviewApproved as DeploymentReviewApproved,
    )
    from .deployment_review_rejected import (
        DeploymentReviewRejected as DeploymentReviewRejected,
    )
    from .discussion_comment_created import (
        DiscussionCommentCreated as DiscussionCommentCreated,
    )
    from .discussion_comment_deleted import (
        DiscussionCommentDeleted as DiscussionCommentDeleted,
    )
    from .registry_package_published import (
        RegistryPackagePublished as RegistryPackagePublished,
    )
    from .repository_ruleset_created import (
        RepositoryRulesetCreated as RepositoryRulesetCreated,
    )
    from .repository_ruleset_deleted import (
        RepositoryRulesetDeleted as RepositoryRulesetDeleted,
    )
    from .code_scanning_alert_created import (
        CodeScanningAlertCreated as CodeScanningAlertCreated,
    )
    from .custom_property_values import (
        CustomPropertyValuesUpdated as CustomPropertyValuesUpdated,
    )
    from .deployment_review_requested import (
        DeploymentReviewRequested as DeploymentReviewRequested,
    )
    from .discussion_category_changed import (
        DiscussionCategoryChanged as DiscussionCategoryChanged,
    )
    from .organization_member_invited import (
        OrganizationMemberInvited as OrganizationMemberInvited,
    )
    from .organization_member_removed import (
        OrganizationMemberRemoved as OrganizationMemberRemoved,
    )
    from .security_advisory_published import (
        SecurityAdvisoryPublished as SecurityAdvisoryPublished,
    )
    from .security_advisory_withdrawn import (
        SecurityAdvisoryWithdrawn as SecurityAdvisoryWithdrawn,
    )
    from .code_scanning_alert_reopened import (
        CodeScanningAlertReopened as CodeScanningAlertReopened,
    )
    from .merge_group_checks_requested import (
        MergeGroupChecksRequested as MergeGroupChecksRequested,
    )
    from .team_removed_from_repository import (
        TeamRemovedFromRepository as TeamRemovedFromRepository,
    )
    from .pull_request_ready_for_review import (
        PullRequestReadyForReview as PullRequestReadyForReview,
    )
    from .marketplace_purchase_changed import (
        MarketplacePurchaseChanged as MarketplacePurchaseChanged,
    )
    from .repository_advisory_reported import (
        RepositoryAdvisoryReported as RepositoryAdvisoryReported,
    )
    from .branch_protection_rule_edited import (
        BranchProtectionRuleEdited as BranchProtectionRuleEdited,
    )
    from .pull_request_review_dismissed import (
        PullRequestReviewDismissed as PullRequestReviewDismissed,
    )
    from .pull_request_review_requested import (
        PullRequestReviewRequested as PullRequestReviewRequested,
    )
    from .pull_request_review_submitted import (
        PullRequestReviewSubmitted as PullRequestReviewSubmitted,
    )
    from .secret_scanning_alert_created import (
        SecretScanningAlertCreated as SecretScanningAlertCreated,
    )
    from .secret_scanning_alert_revoked import (
        SecretScanningAlertRevoked as SecretScanningAlertRevoked,
    )
    from .github_app_authorization import (
        GithubAppAuthorizationRevoked as GithubAppAuthorizationRevoked,
    )
    from .dependabot_alert_reintroduced import (
        DependabotAlertReintroduced as DependabotAlertReintroduced,
    )
    from .repository_advisory_published import (
        RepositoryAdvisoryPublished as RepositoryAdvisoryPublished,
    )
    from .branch_protection_rule_created import (
        BranchProtectionRuleCreated as BranchProtectionRuleCreated,
    )
    from .branch_protection_rule_deleted import (
        BranchProtectionRuleDeleted as BranchProtectionRuleDeleted,
    )
    from .dependabot_alert_auto_reopened import (
        DependabotAlertAutoReopened as DependabotAlertAutoReopened,
    )
    from .secret_scanning_alert_reopened import (
        SecretScanningAlertReopened as SecretScanningAlertReopened,
    )
    from .secret_scanning_alert_resolved import (
        SecretScanningAlertResolved as SecretScanningAlertResolved,
    )
    from .pull_request_auto_merge_enabled import (
        PullRequestAutoMergeEnabled as PullRequestAutoMergeEnabled,
    )
    from .pull_request_converted_to_draft import (
        PullRequestConvertedToDraft as PullRequestConvertedToDraft,
    )
    from .marketplace_purchase_cancelled import (
        MarketplacePurchaseCancelled as MarketplacePurchaseCancelled,
    )
    from .marketplace_purchase_purchased import (
        MarketplacePurchasePurchased as MarketplacePurchasePurchased,
    )
    from .dependabot_alert_auto_dismissed import (
        DependabotAlertAutoDismissed as DependabotAlertAutoDismissed,
    )
    from .sponsorship_pending_tier_change import (
        SponsorshipPendingTierChange as SponsorshipPendingTierChange,
    )
    from .pull_request_auto_merge_disabled import (
        PullRequestAutoMergeDisabled as PullRequestAutoMergeDisabled,
    )
    from .installation_repositories_added import (
        InstallationRepositoriesAdded as InstallationRepositoriesAdded,
    )
    from .code_scanning_alert_closed_by_user import (
        CodeScanningAlertClosedByUser as CodeScanningAlertClosedByUser,
    )
    from .deployment_protection_rule import (
        DeploymentProtectionRuleRequested as DeploymentProtectionRuleRequested,
    )
    from .sponsorship_pending_cancellation import (
        SponsorshipPendingCancellation as SponsorshipPendingCancellation,
    )
    from .pull_request_review_comment_edited import (
        PullRequestReviewCommentEdited as PullRequestReviewCommentEdited,
    )
    from .installation_repositories_removed import (
        InstallationRepositoriesRemoved as InstallationRepositoriesRemoved,
    )
    from .pull_request_review_comment_created import (
        PullRequestReviewCommentCreated as PullRequestReviewCommentCreated,
    )
    from .pull_request_review_comment_deleted import (
        PullRequestReviewCommentDeleted as PullRequestReviewCommentDeleted,
    )
    from .pull_request_review_request_removed import (
        PullRequestReviewRequestRemoved as PullRequestReviewRequestRemoved,
    )
    from .pull_request_review_thread_resolved import (
        PullRequestReviewThreadResolved as PullRequestReviewThreadResolved,
    )
    from .code_scanning_alert_reopened_by_user import (
        CodeScanningAlertReopenedByUser as CodeScanningAlertReopenedByUser,
    )
    from .secret_scanning_alert_location import (
        SecretScanningAlertLocationCreated as SecretScanningAlertLocationCreated,
    )
    from .marketplace_purchase_pending_change import (
        MarketplacePurchasePendingChange as MarketplacePurchasePendingChange,
    )
    from .personal_access_token_request_denied import (
        PersonalAccessTokenRequestDenied as PersonalAccessTokenRequestDenied,
    )
    from .personal_access_token_request_created import (
        PersonalAccessTokenRequestCreated as PersonalAccessTokenRequestCreated,
    )
    from .pull_request_review_thread_unresolved import (
        PullRequestReviewThreadUnresolved as PullRequestReviewThreadUnresolved,
    )
    from .code_scanning_alert_appeared_in_branch import (
        CodeScanningAlertAppearedInBranch as CodeScanningAlertAppearedInBranch,
    )
    from .installation_new_permissions_accepted import (
        InstallationNewPermissionsAccepted as InstallationNewPermissionsAccepted,
    )
    from .repository_vulnerability_alert_create import (
        RepositoryVulnerabilityAlertCreate as RepositoryVulnerabilityAlertCreate,
    )
    from .repository_vulnerability_alert_reopen import (
        RepositoryVulnerabilityAlertReopen as RepositoryVulnerabilityAlertReopen,
    )
    from .personal_access_token_request_approved import (
        PersonalAccessTokenRequestApproved as PersonalAccessTokenRequestApproved,
    )
    from .repository_vulnerability_alert_dismiss import (
        RepositoryVulnerabilityAlertDismiss as RepositoryVulnerabilityAlertDismiss,
    )
    from .repository_vulnerability_alert_resolve import (
        RepositoryVulnerabilityAlertResolve as RepositoryVulnerabilityAlertResolve,
    )
    from .personal_access_token_request_cancelled import (
        PersonalAccessTokenRequestCancelled as PersonalAccessTokenRequestCancelled,
    )
    from .branch_protection_configuration_enabled import (
        BranchProtectionConfigurationEnabled as BranchProtectionConfigurationEnabled,
    )
    from .branch_protection_configuration_disabled import (
        BranchProtectionConfigurationDisabled as BranchProtectionConfigurationDisabled,
    )
    from .marketplace_purchase_pending_change_cancelled import (
        MarketplacePurchasePendingChangeCancelled as MarketplacePurchasePendingChangeCancelled,
    )


else:
    __lazy_vars__ = {
        ".branch_protection_configuration_disabled": (
            "BranchProtectionConfigurationDisabled",
        ),
        ".branch_protection_configuration_enabled": (
            "BranchProtectionConfigurationEnabled",
        ),
        ".branch_protection_rule_created": ("BranchProtectionRuleCreated",),
        ".branch_protection_rule_deleted": ("BranchProtectionRuleDeleted",),
        ".branch_protection_rule_edited": ("BranchProtectionRuleEdited",),
        ".check_run_completed": ("CheckRunCompleted",),
        ".check_run_created": ("CheckRunCreated",),
        ".check_run_requested_action": ("CheckRunRequestedAction",),
        ".check_run_rerequested": ("CheckRunRerequested",),
        ".check_suite_completed": ("CheckSuiteCompleted",),
        ".check_suite_requested": ("CheckSuiteRequested",),
        ".check_suite_rerequested": ("CheckSuiteRerequested",),
        ".code_scanning_alert_appeared_in_branch": (
            "CodeScanningAlertAppearedInBranch",
        ),
        ".code_scanning_alert_closed_by_user": ("CodeScanningAlertClosedByUser",),
        ".code_scanning_alert_created": ("CodeScanningAlertCreated",),
        ".code_scanning_alert_fixed": ("CodeScanningAlertFixed",),
        ".code_scanning_alert_reopened": ("CodeScanningAlertReopened",),
        ".code_scanning_alert_reopened_by_user": ("CodeScanningAlertReopenedByUser",),
        ".commit_comment": ("CommitCommentCreated",),
        ".create": ("Create",),
        ".custom_property_created": ("CustomPropertyCreated",),
        ".custom_property_deleted": ("CustomPropertyDeleted",),
        ".custom_property_updated": ("CustomPropertyUpdated",),
        ".custom_property_values": ("CustomPropertyValuesUpdated",),
        ".delete": ("Delete",),
        ".dependabot_alert_auto_dismissed": ("DependabotAlertAutoDismissed",),
        ".dependabot_alert_auto_reopened": ("DependabotAlertAutoReopened",),
        ".dependabot_alert_created": ("DependabotAlertCreated",),
        ".dependabot_alert_dismissed": ("DependabotAlertDismissed",),
        ".dependabot_alert_fixed": ("DependabotAlertFixed",),
        ".dependabot_alert_reintroduced": ("DependabotAlertReintroduced",),
        ".dependabot_alert_reopened": ("DependabotAlertReopened",),
        ".deploy_key_created": ("DeployKeyCreated",),
        ".deploy_key_deleted": ("DeployKeyDeleted",),
        ".deployment": ("DeploymentCreated",),
        ".deployment_protection_rule": ("DeploymentProtectionRuleRequested",),
        ".deployment_review_approved": ("DeploymentReviewApproved",),
        ".deployment_review_rejected": ("DeploymentReviewRejected",),
        ".deployment_review_requested": ("DeploymentReviewRequested",),
        ".deployment_status": ("DeploymentStatusCreated",),
        ".discussion_answered": ("DiscussionAnswered",),
        ".discussion_category_changed": ("DiscussionCategoryChanged",),
        ".discussion_closed": ("DiscussionClosed",),
        ".discussion_created": ("DiscussionCreated",),
        ".discussion_deleted": ("DiscussionDeleted",),
        ".discussion_edited": ("DiscussionEdited",),
        ".discussion_labeled": ("DiscussionLabeled",),
        ".discussion_locked": ("DiscussionLocked",),
        ".discussion_pinned": ("DiscussionPinned",),
        ".discussion_reopened": ("DiscussionReopened",),
        ".discussion_transferred": ("DiscussionTransferred",),
        ".discussion_unanswered": ("DiscussionUnanswered",),
        ".discussion_unlabeled": ("DiscussionUnlabeled",),
        ".discussion_unlocked": ("DiscussionUnlocked",),
        ".discussion_unpinned": ("DiscussionUnpinned",),
        ".discussion_comment_created": ("DiscussionCommentCreated",),
        ".discussion_comment_deleted": ("DiscussionCommentDeleted",),
        ".discussion_comment_edited": ("DiscussionCommentEdited",),
        ".fork": ("Fork",),
        ".github_app_authorization": ("GithubAppAuthorizationRevoked",),
        ".gollum": ("Gollum",),
        ".installation_created": ("InstallationCreated",),
        ".installation_deleted": ("InstallationDeleted",),
        ".installation_new_permissions_accepted": (
            "InstallationNewPermissionsAccepted",
        ),
        ".installation_suspend": ("InstallationSuspend",),
        ".installation_unsuspend": ("InstallationUnsuspend",),
        ".installation_repositories_added": ("InstallationRepositoriesAdded",),
        ".installation_repositories_removed": ("InstallationRepositoriesRemoved",),
        ".installation_target": ("InstallationTargetRenamed",),
        ".issue_comment_created": ("IssueCommentCreated",),
        ".issue_comment_deleted": ("IssueCommentDeleted",),
        ".issue_comment_edited": ("IssueCommentEdited",),
        ".issues_assigned": ("IssuesAssigned",),
        ".issues_closed": ("IssuesClosed",),
        ".issues_deleted": ("IssuesDeleted",),
        ".issues_demilestoned": ("IssuesDemilestoned",),
        ".issues_edited": ("IssuesEdited",),
        ".issues_labeled": ("IssuesLabeled",),
        ".issues_locked": ("IssuesLocked",),
        ".issues_milestoned": ("IssuesMilestoned",),
        ".issues_opened": ("IssuesOpened",),
        ".issues_pinned": ("IssuesPinned",),
        ".issues_reopened": ("IssuesReopened",),
        ".issues_transferred": ("IssuesTransferred",),
        ".issues_unassigned": ("IssuesUnassigned",),
        ".issues_unlabeled": ("IssuesUnlabeled",),
        ".issues_unlocked": ("IssuesUnlocked",),
        ".issues_unpinned": ("IssuesUnpinned",),
        ".label_created": ("LabelCreated",),
        ".label_deleted": ("LabelDeleted",),
        ".label_edited": ("LabelEdited",),
        ".marketplace_purchase_cancelled": ("MarketplacePurchaseCancelled",),
        ".marketplace_purchase_changed": ("MarketplacePurchaseChanged",),
        ".marketplace_purchase_pending_change": ("MarketplacePurchasePendingChange",),
        ".marketplace_purchase_pending_change_cancelled": (
            "MarketplacePurchasePendingChangeCancelled",
        ),
        ".marketplace_purchase_purchased": ("MarketplacePurchasePurchased",),
        ".member_added": ("MemberAdded",),
        ".member_edited": ("MemberEdited",),
        ".member_removed": ("MemberRemoved",),
        ".membership_added": ("MembershipAdded",),
        ".membership_removed": ("MembershipRemoved",),
        ".merge_group_checks_requested": ("MergeGroupChecksRequested",),
        ".merge_group_destroyed": ("MergeGroupDestroyed",),
        ".meta": ("MetaDeleted",),
        ".milestone_closed": ("MilestoneClosed",),
        ".milestone_created": ("MilestoneCreated",),
        ".milestone_deleted": ("MilestoneDeleted",),
        ".milestone_edited": ("MilestoneEdited",),
        ".milestone_opened": ("MilestoneOpened",),
        ".org_block_blocked": ("OrgBlockBlocked",),
        ".org_block_unblocked": ("OrgBlockUnblocked",),
        ".organization_deleted": ("OrganizationDeleted",),
        ".organization_member_added": ("OrganizationMemberAdded",),
        ".organization_member_invited": ("OrganizationMemberInvited",),
        ".organization_member_removed": ("OrganizationMemberRemoved",),
        ".organization_renamed": ("OrganizationRenamed",),
        ".package_published": ("PackagePublished",),
        ".package_updated": ("PackageUpdated",),
        ".page_build": ("PageBuild",),
        ".personal_access_token_request_approved": (
            "PersonalAccessTokenRequestApproved",
        ),
        ".personal_access_token_request_cancelled": (
            "PersonalAccessTokenRequestCancelled",
        ),
        ".personal_access_token_request_created": (
            "PersonalAccessTokenRequestCreated",
        ),
        ".personal_access_token_request_denied": ("PersonalAccessTokenRequestDenied",),
        ".ping": ("Ping",),
        ".project_card_converted": ("ProjectCardConverted",),
        ".project_card_created": ("ProjectCardCreated",),
        ".project_card_deleted": ("ProjectCardDeleted",),
        ".project_card_edited": ("ProjectCardEdited",),
        ".project_card_moved": ("ProjectCardMoved",),
        ".project_closed": ("ProjectClosed",),
        ".project_created": ("ProjectCreated",),
        ".project_deleted": ("ProjectDeleted",),
        ".project_edited": ("ProjectEdited",),
        ".project_reopened": ("ProjectReopened",),
        ".project_column_created": ("ProjectColumnCreated",),
        ".project_column_deleted": ("ProjectColumnDeleted",),
        ".project_column_edited": ("ProjectColumnEdited",),
        ".project_column_moved": ("ProjectColumnMoved",),
        ".projects_v2_closed": ("ProjectsV2ProjectClosed",),
        ".projects_v2_created": ("ProjectsV2ProjectCreated",),
        ".projects_v2_deleted": ("ProjectsV2ProjectDeleted",),
        ".projects_v2_edited": ("ProjectsV2ProjectEdited",),
        ".projects_v2_reopened": ("ProjectsV2ProjectReopened",),
        ".projects_v2_item_archived": ("ProjectsV2ItemArchived",),
        ".projects_v2_item_converted": ("ProjectsV2ItemConverted",),
        ".projects_v2_item_created": ("ProjectsV2ItemCreated",),
        ".projects_v2_item_deleted": ("ProjectsV2ItemDeleted",),
        ".projects_v2_item_edited": ("ProjectsV2ItemEdited",),
        ".projects_v2_item_reordered": ("ProjectsV2ItemReordered",),
        ".projects_v2_item_restored": ("ProjectsV2ItemRestored",),
        ".public": ("Public",),
        ".pull_request_assigned": ("PullRequestAssigned",),
        ".pull_request_auto_merge_disabled": ("PullRequestAutoMergeDisabled",),
        ".pull_request_auto_merge_enabled": ("PullRequestAutoMergeEnabled",),
        ".pull_request_closed": ("PullRequestClosed",),
        ".pull_request_converted_to_draft": ("PullRequestConvertedToDraft",),
        ".pull_request_demilestoned": ("PullRequestDemilestoned",),
        ".pull_request_dequeued": ("PullRequestDequeued",),
        ".pull_request_edited": ("PullRequestEdited",),
        ".pull_request_enqueued": ("PullRequestEnqueued",),
        ".pull_request_labeled": ("PullRequestLabeled",),
        ".pull_request_locked": ("PullRequestLocked",),
        ".pull_request_milestoned": ("PullRequestMilestoned",),
        ".pull_request_opened": ("PullRequestOpened",),
        ".pull_request_ready_for_review": ("PullRequestReadyForReview",),
        ".pull_request_reopened": ("PullRequestReopened",),
        ".pull_request_review_request_removed": ("PullRequestReviewRequestRemoved",),
        ".pull_request_review_requested": ("PullRequestReviewRequested",),
        ".pull_request_synchronize": ("PullRequestSynchronize",),
        ".pull_request_unassigned": ("PullRequestUnassigned",),
        ".pull_request_unlabeled": ("PullRequestUnlabeled",),
        ".pull_request_unlocked": ("PullRequestUnlocked",),
        ".pull_request_review_comment_created": ("PullRequestReviewCommentCreated",),
        ".pull_request_review_comment_deleted": ("PullRequestReviewCommentDeleted",),
        ".pull_request_review_comment_edited": ("PullRequestReviewCommentEdited",),
        ".pull_request_review_dismissed": ("PullRequestReviewDismissed",),
        ".pull_request_review_edited": ("PullRequestReviewEdited",),
        ".pull_request_review_submitted": ("PullRequestReviewSubmitted",),
        ".pull_request_review_thread_resolved": ("PullRequestReviewThreadResolved",),
        ".pull_request_review_thread_unresolved": (
            "PullRequestReviewThreadUnresolved",
        ),
        ".push": ("Push",),
        ".registry_package_published": ("RegistryPackagePublished",),
        ".registry_package_updated": ("RegistryPackageUpdated",),
        ".release_created": ("ReleaseCreated",),
        ".release_deleted": ("ReleaseDeleted",),
        ".release_edited": ("ReleaseEdited",),
        ".release_prereleased": ("ReleasePrereleased",),
        ".release_published": ("ReleasePublished",),
        ".release_released": ("ReleaseReleased",),
        ".release_unpublished": ("ReleaseUnpublished",),
        ".repository_advisory_published": ("RepositoryAdvisoryPublished",),
        ".repository_advisory_reported": ("RepositoryAdvisoryReported",),
        ".repository_archived": ("RepositoryArchived",),
        ".repository_created": ("RepositoryCreated",),
        ".repository_deleted": ("RepositoryDeleted",),
        ".repository_edited": ("RepositoryEdited",),
        ".repository_privatized": ("RepositoryPrivatized",),
        ".repository_publicized": ("RepositoryPublicized",),
        ".repository_renamed": ("RepositoryRenamed",),
        ".repository_transferred": ("RepositoryTransferred",),
        ".repository_unarchived": ("RepositoryUnarchived",),
        ".repository_dispatch": ("RepositoryDispatchSample",),
        ".repository_import": ("RepositoryImport",),
        ".repository_ruleset_created": ("RepositoryRulesetCreated",),
        ".repository_ruleset_deleted": ("RepositoryRulesetDeleted",),
        ".repository_ruleset_edited": ("RepositoryRulesetEdited",),
        ".repository_vulnerability_alert_create": (
            "RepositoryVulnerabilityAlertCreate",
        ),
        ".repository_vulnerability_alert_dismiss": (
            "RepositoryVulnerabilityAlertDismiss",
        ),
        ".repository_vulnerability_alert_reopen": (
            "RepositoryVulnerabilityAlertReopen",
        ),
        ".repository_vulnerability_alert_resolve": (
            "RepositoryVulnerabilityAlertResolve",
        ),
        ".secret_scanning_alert_created": ("SecretScanningAlertCreated",),
        ".secret_scanning_alert_reopened": ("SecretScanningAlertReopened",),
        ".secret_scanning_alert_resolved": ("SecretScanningAlertResolved",),
        ".secret_scanning_alert_revoked": ("SecretScanningAlertRevoked",),
        ".secret_scanning_alert_location": ("SecretScanningAlertLocationCreated",),
        ".security_advisory_published": ("SecurityAdvisoryPublished",),
        ".security_advisory_updated": ("SecurityAdvisoryUpdated",),
        ".security_advisory_withdrawn": ("SecurityAdvisoryWithdrawn",),
        ".security_and_analysis": ("SecurityAndAnalysis",),
        ".sponsorship_cancelled": ("SponsorshipCancelled",),
        ".sponsorship_created": ("SponsorshipCreated",),
        ".sponsorship_edited": ("SponsorshipEdited",),
        ".sponsorship_pending_cancellation": ("SponsorshipPendingCancellation",),
        ".sponsorship_pending_tier_change": ("SponsorshipPendingTierChange",),
        ".sponsorship_tier_changed": ("SponsorshipTierChanged",),
        ".star_created": ("StarCreated",),
        ".star_deleted": ("StarDeleted",),
        ".status": ("Status",),
        ".team_add": ("TeamAdd",),
        ".team_added_to_repository": ("TeamAddedToRepository",),
        ".team_created": ("TeamCreated",),
        ".team_deleted": ("TeamDeleted",),
        ".team_edited": ("TeamEdited",),
        ".team_removed_from_repository": ("TeamRemovedFromRepository",),
        ".watch": ("WatchStarted",),
        ".workflow_dispatch": ("WorkflowDispatch",),
        ".workflow_job_completed": ("WorkflowJobCompleted",),
        ".workflow_job_in_progress": ("WorkflowJobInProgress",),
        ".workflow_job_queued": ("WorkflowJobQueued",),
        ".workflow_job_waiting": ("WorkflowJobWaiting",),
        ".workflow_run_completed": ("WorkflowRunCompleted",),
        ".workflow_run_in_progress": ("WorkflowRunInProgress",),
        ".workflow_run_requested": ("WorkflowRunRequested",),
        "._base": ("Event",),
        "._types": ("events",),
    }
