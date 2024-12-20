from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._base import Event as Event
    from ._types import events as events
    from .branch_protection_configuration_disabled import (
        BranchProtectionConfigurationDisabled as BranchProtectionConfigurationDisabled,
    )
    from .branch_protection_configuration_enabled import (
        BranchProtectionConfigurationEnabled as BranchProtectionConfigurationEnabled,
    )
    from .branch_protection_rule_created import (
        BranchProtectionRuleCreated as BranchProtectionRuleCreated,
    )
    from .branch_protection_rule_deleted import (
        BranchProtectionRuleDeleted as BranchProtectionRuleDeleted,
    )
    from .branch_protection_rule_edited import (
        BranchProtectionRuleEdited as BranchProtectionRuleEdited,
    )
    from .check_run_completed import CheckRunCompleted as CheckRunCompleted
    from .check_run_created import CheckRunCreated as CheckRunCreated
    from .check_run_requested_action import (
        CheckRunRequestedAction as CheckRunRequestedAction,
    )
    from .check_run_rerequested import CheckRunRerequested as CheckRunRerequested
    from .check_suite_completed import CheckSuiteCompleted as CheckSuiteCompleted
    from .check_suite_requested import CheckSuiteRequested as CheckSuiteRequested
    from .check_suite_rerequested import CheckSuiteRerequested as CheckSuiteRerequested
    from .code_scanning_alert_appeared_in_branch import (
        CodeScanningAlertAppearedInBranch as CodeScanningAlertAppearedInBranch,
    )
    from .code_scanning_alert_closed_by_user import (
        CodeScanningAlertClosedByUser as CodeScanningAlertClosedByUser,
    )
    from .code_scanning_alert_created import (
        CodeScanningAlertCreated as CodeScanningAlertCreated,
    )
    from .code_scanning_alert_fixed import (
        CodeScanningAlertFixed as CodeScanningAlertFixed,
    )
    from .code_scanning_alert_reopened import (
        CodeScanningAlertReopened as CodeScanningAlertReopened,
    )
    from .code_scanning_alert_reopened_by_user import (
        CodeScanningAlertReopenedByUser as CodeScanningAlertReopenedByUser,
    )
    from .commit_comment import CommitCommentCreated as CommitCommentCreated
    from .create import Create as Create
    from .custom_property_created import CustomPropertyCreated as CustomPropertyCreated
    from .custom_property_deleted import CustomPropertyDeleted as CustomPropertyDeleted
    from .custom_property_updated import CustomPropertyUpdated as CustomPropertyUpdated
    from .custom_property_values import (
        CustomPropertyValuesUpdated as CustomPropertyValuesUpdated,
    )
    from .delete import Delete as Delete
    from .dependabot_alert_auto_dismissed import (
        DependabotAlertAutoDismissed as DependabotAlertAutoDismissed,
    )
    from .dependabot_alert_auto_reopened import (
        DependabotAlertAutoReopened as DependabotAlertAutoReopened,
    )
    from .dependabot_alert_created import (
        DependabotAlertCreated as DependabotAlertCreated,
    )
    from .dependabot_alert_dismissed import (
        DependabotAlertDismissed as DependabotAlertDismissed,
    )
    from .dependabot_alert_fixed import DependabotAlertFixed as DependabotAlertFixed
    from .dependabot_alert_reintroduced import (
        DependabotAlertReintroduced as DependabotAlertReintroduced,
    )
    from .dependabot_alert_reopened import (
        DependabotAlertReopened as DependabotAlertReopened,
    )
    from .deploy_key_created import DeployKeyCreated as DeployKeyCreated
    from .deploy_key_deleted import DeployKeyDeleted as DeployKeyDeleted
    from .deployment import DeploymentCreated as DeploymentCreated
    from .deployment_protection_rule import (
        DeploymentProtectionRuleRequested as DeploymentProtectionRuleRequested,
    )
    from .deployment_review_approved import (
        DeploymentReviewApproved as DeploymentReviewApproved,
    )
    from .deployment_review_rejected import (
        DeploymentReviewRejected as DeploymentReviewRejected,
    )
    from .deployment_review_requested import (
        DeploymentReviewRequested as DeploymentReviewRequested,
    )
    from .deployment_status import DeploymentStatusCreated as DeploymentStatusCreated
    from .discussion_answered import DiscussionAnswered as DiscussionAnswered
    from .discussion_category_changed import (
        DiscussionCategoryChanged as DiscussionCategoryChanged,
    )
    from .discussion_closed import DiscussionClosed as DiscussionClosed
    from .discussion_comment_created import (
        DiscussionCommentCreated as DiscussionCommentCreated,
    )
    from .discussion_comment_deleted import (
        DiscussionCommentDeleted as DiscussionCommentDeleted,
    )
    from .discussion_comment_edited import (
        DiscussionCommentEdited as DiscussionCommentEdited,
    )
    from .discussion_created import DiscussionCreated as DiscussionCreated
    from .discussion_deleted import DiscussionDeleted as DiscussionDeleted
    from .discussion_edited import DiscussionEdited as DiscussionEdited
    from .discussion_labeled import DiscussionLabeled as DiscussionLabeled
    from .discussion_locked import DiscussionLocked as DiscussionLocked
    from .discussion_pinned import DiscussionPinned as DiscussionPinned
    from .discussion_reopened import DiscussionReopened as DiscussionReopened
    from .discussion_transferred import DiscussionTransferred as DiscussionTransferred
    from .discussion_unanswered import DiscussionUnanswered as DiscussionUnanswered
    from .discussion_unlabeled import DiscussionUnlabeled as DiscussionUnlabeled
    from .discussion_unlocked import DiscussionUnlocked as DiscussionUnlocked
    from .discussion_unpinned import DiscussionUnpinned as DiscussionUnpinned
    from .fork import Fork as Fork
    from .github_app_authorization import (
        GithubAppAuthorizationRevoked as GithubAppAuthorizationRevoked,
    )
    from .gollum import Gollum as Gollum
    from .installation_created import InstallationCreated as InstallationCreated
    from .installation_deleted import InstallationDeleted as InstallationDeleted
    from .installation_new_permissions_accepted import (
        InstallationNewPermissionsAccepted as InstallationNewPermissionsAccepted,
    )
    from .installation_repositories_added import (
        InstallationRepositoriesAdded as InstallationRepositoriesAdded,
    )
    from .installation_repositories_removed import (
        InstallationRepositoriesRemoved as InstallationRepositoriesRemoved,
    )
    from .installation_suspend import InstallationSuspend as InstallationSuspend
    from .installation_target import (
        InstallationTargetRenamed as InstallationTargetRenamed,
    )
    from .installation_unsuspend import InstallationUnsuspend as InstallationUnsuspend
    from .issue_comment_created import IssueCommentCreated as IssueCommentCreated
    from .issue_comment_deleted import IssueCommentDeleted as IssueCommentDeleted
    from .issue_comment_edited import IssueCommentEdited as IssueCommentEdited
    from .issues_assigned import IssuesAssigned as IssuesAssigned
    from .issues_closed import IssuesClosed as IssuesClosed
    from .issues_deleted import IssuesDeleted as IssuesDeleted
    from .issues_demilestoned import IssuesDemilestoned as IssuesDemilestoned
    from .issues_edited import IssuesEdited as IssuesEdited
    from .issues_labeled import IssuesLabeled as IssuesLabeled
    from .issues_locked import IssuesLocked as IssuesLocked
    from .issues_milestoned import IssuesMilestoned as IssuesMilestoned
    from .issues_opened import IssuesOpened as IssuesOpened
    from .issues_pinned import IssuesPinned as IssuesPinned
    from .issues_reopened import IssuesReopened as IssuesReopened
    from .issues_transferred import IssuesTransferred as IssuesTransferred
    from .issues_unassigned import IssuesUnassigned as IssuesUnassigned
    from .issues_unlabeled import IssuesUnlabeled as IssuesUnlabeled
    from .issues_unlocked import IssuesUnlocked as IssuesUnlocked
    from .issues_unpinned import IssuesUnpinned as IssuesUnpinned
    from .label_created import LabelCreated as LabelCreated
    from .label_deleted import LabelDeleted as LabelDeleted
    from .label_edited import LabelEdited as LabelEdited
    from .marketplace_purchase_cancelled import (
        MarketplacePurchaseCancelled as MarketplacePurchaseCancelled,
    )
    from .marketplace_purchase_changed import (
        MarketplacePurchaseChanged as MarketplacePurchaseChanged,
    )
    from .marketplace_purchase_pending_change import (
        MarketplacePurchasePendingChange as MarketplacePurchasePendingChange,
    )
    from .marketplace_purchase_pending_change_cancelled import (
        MarketplacePurchasePendingChangeCancelled as MarketplacePurchasePendingChangeCancelled,
    )
    from .marketplace_purchase_purchased import (
        MarketplacePurchasePurchased as MarketplacePurchasePurchased,
    )
    from .member_added import MemberAdded as MemberAdded
    from .member_edited import MemberEdited as MemberEdited
    from .member_removed import MemberRemoved as MemberRemoved
    from .membership_added import MembershipAdded as MembershipAdded
    from .membership_removed import MembershipRemoved as MembershipRemoved
    from .merge_group_checks_requested import (
        MergeGroupChecksRequested as MergeGroupChecksRequested,
    )
    from .merge_group_destroyed import MergeGroupDestroyed as MergeGroupDestroyed
    from .meta import MetaDeleted as MetaDeleted
    from .milestone_closed import MilestoneClosed as MilestoneClosed
    from .milestone_created import MilestoneCreated as MilestoneCreated
    from .milestone_deleted import MilestoneDeleted as MilestoneDeleted
    from .milestone_edited import MilestoneEdited as MilestoneEdited
    from .milestone_opened import MilestoneOpened as MilestoneOpened
    from .org_block_blocked import OrgBlockBlocked as OrgBlockBlocked
    from .org_block_unblocked import OrgBlockUnblocked as OrgBlockUnblocked
    from .organization_deleted import OrganizationDeleted as OrganizationDeleted
    from .organization_member_added import (
        OrganizationMemberAdded as OrganizationMemberAdded,
    )
    from .organization_member_invited import (
        OrganizationMemberInvited as OrganizationMemberInvited,
    )
    from .organization_member_removed import (
        OrganizationMemberRemoved as OrganizationMemberRemoved,
    )
    from .organization_renamed import OrganizationRenamed as OrganizationRenamed
    from .package_published import PackagePublished as PackagePublished
    from .package_updated import PackageUpdated as PackageUpdated
    from .page_build import PageBuild as PageBuild
    from .personal_access_token_request_approved import (
        PersonalAccessTokenRequestApproved as PersonalAccessTokenRequestApproved,
    )
    from .personal_access_token_request_cancelled import (
        PersonalAccessTokenRequestCancelled as PersonalAccessTokenRequestCancelled,
    )
    from .personal_access_token_request_created import (
        PersonalAccessTokenRequestCreated as PersonalAccessTokenRequestCreated,
    )
    from .personal_access_token_request_denied import (
        PersonalAccessTokenRequestDenied as PersonalAccessTokenRequestDenied,
    )
    from .ping import Ping as Ping
    from .project_card_converted import ProjectCardConverted as ProjectCardConverted
    from .project_card_created import ProjectCardCreated as ProjectCardCreated
    from .project_card_deleted import ProjectCardDeleted as ProjectCardDeleted
    from .project_card_edited import ProjectCardEdited as ProjectCardEdited
    from .project_card_moved import ProjectCardMoved as ProjectCardMoved
    from .project_closed import ProjectClosed as ProjectClosed
    from .project_column_created import ProjectColumnCreated as ProjectColumnCreated
    from .project_column_deleted import ProjectColumnDeleted as ProjectColumnDeleted
    from .project_column_edited import ProjectColumnEdited as ProjectColumnEdited
    from .project_column_moved import ProjectColumnMoved as ProjectColumnMoved
    from .project_created import ProjectCreated as ProjectCreated
    from .project_deleted import ProjectDeleted as ProjectDeleted
    from .project_edited import ProjectEdited as ProjectEdited
    from .project_reopened import ProjectReopened as ProjectReopened
    from .projects_v2_closed import ProjectsV2ProjectClosed as ProjectsV2ProjectClosed
    from .projects_v2_created import (
        ProjectsV2ProjectCreated as ProjectsV2ProjectCreated,
    )
    from .projects_v2_deleted import (
        ProjectsV2ProjectDeleted as ProjectsV2ProjectDeleted,
    )
    from .projects_v2_edited import ProjectsV2ProjectEdited as ProjectsV2ProjectEdited
    from .projects_v2_item_archived import (
        ProjectsV2ItemArchived as ProjectsV2ItemArchived,
    )
    from .projects_v2_item_converted import (
        ProjectsV2ItemConverted as ProjectsV2ItemConverted,
    )
    from .projects_v2_item_created import ProjectsV2ItemCreated as ProjectsV2ItemCreated
    from .projects_v2_item_deleted import ProjectsV2ItemDeleted as ProjectsV2ItemDeleted
    from .projects_v2_item_edited import ProjectsV2ItemEdited as ProjectsV2ItemEdited
    from .projects_v2_item_reordered import (
        ProjectsV2ItemReordered as ProjectsV2ItemReordered,
    )
    from .projects_v2_item_restored import (
        ProjectsV2ItemRestored as ProjectsV2ItemRestored,
    )
    from .projects_v2_reopened import (
        ProjectsV2ProjectReopened as ProjectsV2ProjectReopened,
    )
    from .projects_v2_status_update_created import (
        ProjectsV2StatusUpdateCreated as ProjectsV2StatusUpdateCreated,
    )
    from .projects_v2_status_update_deleted import (
        ProjectsV2StatusUpdateDeleted as ProjectsV2StatusUpdateDeleted,
    )
    from .projects_v2_status_update_edited import (
        ProjectsV2StatusUpdateEdited as ProjectsV2StatusUpdateEdited,
    )
    from .public import Public as Public
    from .pull_request_assigned import PullRequestAssigned as PullRequestAssigned
    from .pull_request_auto_merge_disabled import (
        PullRequestAutoMergeDisabled as PullRequestAutoMergeDisabled,
    )
    from .pull_request_auto_merge_enabled import (
        PullRequestAutoMergeEnabled as PullRequestAutoMergeEnabled,
    )
    from .pull_request_closed import PullRequestClosed as PullRequestClosed
    from .pull_request_converted_to_draft import (
        PullRequestConvertedToDraft as PullRequestConvertedToDraft,
    )
    from .pull_request_demilestoned import (
        PullRequestDemilestoned as PullRequestDemilestoned,
    )
    from .pull_request_dequeued import PullRequestDequeued as PullRequestDequeued
    from .pull_request_edited import PullRequestEdited as PullRequestEdited
    from .pull_request_enqueued import PullRequestEnqueued as PullRequestEnqueued
    from .pull_request_labeled import PullRequestLabeled as PullRequestLabeled
    from .pull_request_locked import PullRequestLocked as PullRequestLocked
    from .pull_request_milestoned import PullRequestMilestoned as PullRequestMilestoned
    from .pull_request_opened import PullRequestOpened as PullRequestOpened
    from .pull_request_ready_for_review import (
        PullRequestReadyForReview as PullRequestReadyForReview,
    )
    from .pull_request_reopened import PullRequestReopened as PullRequestReopened
    from .pull_request_review_comment_created import (
        PullRequestReviewCommentCreated as PullRequestReviewCommentCreated,
    )
    from .pull_request_review_comment_deleted import (
        PullRequestReviewCommentDeleted as PullRequestReviewCommentDeleted,
    )
    from .pull_request_review_comment_edited import (
        PullRequestReviewCommentEdited as PullRequestReviewCommentEdited,
    )
    from .pull_request_review_dismissed import (
        PullRequestReviewDismissed as PullRequestReviewDismissed,
    )
    from .pull_request_review_edited import (
        PullRequestReviewEdited as PullRequestReviewEdited,
    )
    from .pull_request_review_request_removed import (
        PullRequestReviewRequestRemoved as PullRequestReviewRequestRemoved,
    )
    from .pull_request_review_requested import (
        PullRequestReviewRequested as PullRequestReviewRequested,
    )
    from .pull_request_review_submitted import (
        PullRequestReviewSubmitted as PullRequestReviewSubmitted,
    )
    from .pull_request_review_thread_resolved import (
        PullRequestReviewThreadResolved as PullRequestReviewThreadResolved,
    )
    from .pull_request_review_thread_unresolved import (
        PullRequestReviewThreadUnresolved as PullRequestReviewThreadUnresolved,
    )
    from .pull_request_synchronize import (
        PullRequestSynchronize as PullRequestSynchronize,
    )
    from .pull_request_unassigned import PullRequestUnassigned as PullRequestUnassigned
    from .pull_request_unlabeled import PullRequestUnlabeled as PullRequestUnlabeled
    from .pull_request_unlocked import PullRequestUnlocked as PullRequestUnlocked
    from .push import Push as Push
    from .registry_package_published import (
        RegistryPackagePublished as RegistryPackagePublished,
    )
    from .registry_package_updated import (
        RegistryPackageUpdated as RegistryPackageUpdated,
    )
    from .release_created import ReleaseCreated as ReleaseCreated
    from .release_deleted import ReleaseDeleted as ReleaseDeleted
    from .release_edited import ReleaseEdited as ReleaseEdited
    from .release_prereleased import ReleasePrereleased as ReleasePrereleased
    from .release_published import ReleasePublished as ReleasePublished
    from .release_released import ReleaseReleased as ReleaseReleased
    from .release_unpublished import ReleaseUnpublished as ReleaseUnpublished
    from .repository_advisory_published import (
        RepositoryAdvisoryPublished as RepositoryAdvisoryPublished,
    )
    from .repository_advisory_reported import (
        RepositoryAdvisoryReported as RepositoryAdvisoryReported,
    )
    from .repository_archived import RepositoryArchived as RepositoryArchived
    from .repository_created import RepositoryCreated as RepositoryCreated
    from .repository_deleted import RepositoryDeleted as RepositoryDeleted
    from .repository_dispatch import (
        RepositoryDispatchSample as RepositoryDispatchSample,
    )
    from .repository_edited import RepositoryEdited as RepositoryEdited
    from .repository_import import RepositoryImport as RepositoryImport
    from .repository_privatized import RepositoryPrivatized as RepositoryPrivatized
    from .repository_publicized import RepositoryPublicized as RepositoryPublicized
    from .repository_renamed import RepositoryRenamed as RepositoryRenamed
    from .repository_ruleset_created import (
        RepositoryRulesetCreated as RepositoryRulesetCreated,
    )
    from .repository_ruleset_deleted import (
        RepositoryRulesetDeleted as RepositoryRulesetDeleted,
    )
    from .repository_ruleset_edited import (
        RepositoryRulesetEdited as RepositoryRulesetEdited,
    )
    from .repository_transferred import RepositoryTransferred as RepositoryTransferred
    from .repository_unarchived import RepositoryUnarchived as RepositoryUnarchived
    from .repository_vulnerability_alert_create import (
        RepositoryVulnerabilityAlertCreate as RepositoryVulnerabilityAlertCreate,
    )
    from .repository_vulnerability_alert_dismiss import (
        RepositoryVulnerabilityAlertDismiss as RepositoryVulnerabilityAlertDismiss,
    )
    from .repository_vulnerability_alert_reopen import (
        RepositoryVulnerabilityAlertReopen as RepositoryVulnerabilityAlertReopen,
    )
    from .repository_vulnerability_alert_resolve import (
        RepositoryVulnerabilityAlertResolve as RepositoryVulnerabilityAlertResolve,
    )
    from .secret_scanning_alert_created import (
        SecretScanningAlertCreated as SecretScanningAlertCreated,
    )
    from .secret_scanning_alert_location import (
        SecretScanningAlertLocationCreated as SecretScanningAlertLocationCreated,
    )
    from .secret_scanning_alert_publicly_leaked import (
        SecretScanningAlertPubliclyLeaked as SecretScanningAlertPubliclyLeaked,
    )
    from .secret_scanning_alert_reopened import (
        SecretScanningAlertReopened as SecretScanningAlertReopened,
    )
    from .secret_scanning_alert_resolved import (
        SecretScanningAlertResolved as SecretScanningAlertResolved,
    )
    from .secret_scanning_alert_validated import (
        SecretScanningAlertValidated as SecretScanningAlertValidated,
    )
    from .secret_scanning_scan import (
        SecretScanningScanCompleted as SecretScanningScanCompleted,
    )
    from .security_advisory_published import (
        SecurityAdvisoryPublished as SecurityAdvisoryPublished,
    )
    from .security_advisory_updated import (
        SecurityAdvisoryUpdated as SecurityAdvisoryUpdated,
    )
    from .security_advisory_withdrawn import (
        SecurityAdvisoryWithdrawn as SecurityAdvisoryWithdrawn,
    )
    from .security_and_analysis import SecurityAndAnalysis as SecurityAndAnalysis
    from .sponsorship_cancelled import SponsorshipCancelled as SponsorshipCancelled
    from .sponsorship_created import SponsorshipCreated as SponsorshipCreated
    from .sponsorship_edited import SponsorshipEdited as SponsorshipEdited
    from .sponsorship_pending_cancellation import (
        SponsorshipPendingCancellation as SponsorshipPendingCancellation,
    )
    from .sponsorship_pending_tier_change import (
        SponsorshipPendingTierChange as SponsorshipPendingTierChange,
    )
    from .sponsorship_tier_changed import (
        SponsorshipTierChanged as SponsorshipTierChanged,
    )
    from .star_created import StarCreated as StarCreated
    from .star_deleted import StarDeleted as StarDeleted
    from .status import Status as Status
    from .sub_issues_parent_issue_added import (
        SubIssuesParentIssueAdded as SubIssuesParentIssueAdded,
    )
    from .sub_issues_parent_issue_removed import (
        SubIssuesParentIssueRemoved as SubIssuesParentIssueRemoved,
    )
    from .sub_issues_sub_issue_added import (
        SubIssuesSubIssueAdded as SubIssuesSubIssueAdded,
    )
    from .sub_issues_sub_issue_removed import (
        SubIssuesSubIssueRemoved as SubIssuesSubIssueRemoved,
    )
    from .team_add import TeamAdd as TeamAdd
    from .team_added_to_repository import TeamAddedToRepository as TeamAddedToRepository
    from .team_created import TeamCreated as TeamCreated
    from .team_deleted import TeamDeleted as TeamDeleted
    from .team_edited import TeamEdited as TeamEdited
    from .team_removed_from_repository import (
        TeamRemovedFromRepository as TeamRemovedFromRepository,
    )
    from .watch import WatchStarted as WatchStarted
    from .workflow_dispatch import WorkflowDispatch as WorkflowDispatch
    from .workflow_job_completed import WorkflowJobCompleted as WorkflowJobCompleted
    from .workflow_job_in_progress import WorkflowJobInProgress as WorkflowJobInProgress
    from .workflow_job_queued import WorkflowJobQueued as WorkflowJobQueued
    from .workflow_job_waiting import WorkflowJobWaiting as WorkflowJobWaiting
    from .workflow_run_completed import WorkflowRunCompleted as WorkflowRunCompleted
    from .workflow_run_in_progress import WorkflowRunInProgress as WorkflowRunInProgress
    from .workflow_run_requested import WorkflowRunRequested as WorkflowRunRequested


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
        ".projects_v2_status_update_created": ("ProjectsV2StatusUpdateCreated",),
        ".projects_v2_status_update_deleted": ("ProjectsV2StatusUpdateDeleted",),
        ".projects_v2_status_update_edited": ("ProjectsV2StatusUpdateEdited",),
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
        ".secret_scanning_alert_publicly_leaked": (
            "SecretScanningAlertPubliclyLeaked",
        ),
        ".secret_scanning_alert_reopened": ("SecretScanningAlertReopened",),
        ".secret_scanning_alert_resolved": ("SecretScanningAlertResolved",),
        ".secret_scanning_alert_validated": ("SecretScanningAlertValidated",),
        ".secret_scanning_alert_location": ("SecretScanningAlertLocationCreated",),
        ".secret_scanning_scan": ("SecretScanningScanCompleted",),
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
        ".sub_issues_parent_issue_added": ("SubIssuesParentIssueAdded",),
        ".sub_issues_parent_issue_removed": ("SubIssuesParentIssueRemoved",),
        ".sub_issues_sub_issue_added": ("SubIssuesSubIssueAdded",),
        ".sub_issues_sub_issue_removed": ("SubIssuesSubIssueRemoved",),
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
