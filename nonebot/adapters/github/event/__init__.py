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
    from .team import TeamEdited as TeamEdited
    from .meta import MetaDeleted as MetaDeleted
    from .star import StarCreated as StarCreated
    from .star import StarDeleted as StarDeleted
    from .team import TeamCreated as TeamCreated
    from .team import TeamDeleted as TeamDeleted
    from .label import LabelEdited as LabelEdited
    from .member import MemberAdded as MemberAdded
    from .page_build import PageBuild as PageBuild
    from .label import LabelCreated as LabelCreated
    from .label import LabelDeleted as LabelDeleted
    from .watch import WatchStarted as WatchStarted
    from .issues import IssuesClosed as IssuesClosed
    from .issues import IssuesEdited as IssuesEdited
    from .issues import IssuesLocked as IssuesLocked
    from .issues import IssuesOpened as IssuesOpened
    from .issues import IssuesPinned as IssuesPinned
    from .member import MemberEdited as MemberEdited
    from .issues import IssuesDeleted as IssuesDeleted
    from .issues import IssuesLabeled as IssuesLabeled
    from .member import MemberRemoved as MemberRemoved
    from .project import ProjectClosed as ProjectClosed
    from .project import ProjectEdited as ProjectEdited
    from .release import ReleaseEdited as ReleaseEdited
    from .issues import IssuesAssigned as IssuesAssigned
    from .issues import IssuesReopened as IssuesReopened
    from .issues import IssuesUnlocked as IssuesUnlocked
    from .issues import IssuesUnpinned as IssuesUnpinned
    from .package import PackageUpdated as PackageUpdated
    from .project import ProjectCreated as ProjectCreated
    from .project import ProjectDeleted as ProjectDeleted
    from .release import ReleaseCreated as ReleaseCreated
    from .release import ReleaseDeleted as ReleaseDeleted
    from .issues import IssuesUnlabeled as IssuesUnlabeled
    from .project import ProjectReopened as ProjectReopened
    from .release import ReleaseReleased as ReleaseReleased
    from .issues import IssuesMilestoned as IssuesMilestoned
    from .issues import IssuesUnassigned as IssuesUnassigned
    from .check_run import CheckRunCreated as CheckRunCreated
    from .milestone import MilestoneClosed as MilestoneClosed
    from .milestone import MilestoneEdited as MilestoneEdited
    from .milestone import MilestoneOpened as MilestoneOpened
    from .org_block import OrgBlockBlocked as OrgBlockBlocked
    from .package import PackagePublished as PackagePublished
    from .release import ReleasePublished as ReleasePublished
    from .issues import IssuesTransferred as IssuesTransferred
    from .membership import MembershipAdded as MembershipAdded
    from .milestone import MilestoneCreated as MilestoneCreated
    from .milestone import MilestoneDeleted as MilestoneDeleted
    from .deploy_key import DeployKeyCreated as DeployKeyCreated
    from .deploy_key import DeployKeyDeleted as DeployKeyDeleted
    from .discussion import DiscussionClosed as DiscussionClosed
    from .discussion import DiscussionEdited as DiscussionEdited
    from .discussion import DiscussionLocked as DiscussionLocked
    from .discussion import DiscussionPinned as DiscussionPinned
    from .issues import IssuesDemilestoned as IssuesDemilestoned
    from .repository import RepositoryEdited as RepositoryEdited
    from .check_run import CheckRunCompleted as CheckRunCompleted
    from .org_block import OrgBlockUnblocked as OrgBlockUnblocked
    from .release import ReleasePrereleased as ReleasePrereleased
    from .release import ReleaseUnpublished as ReleaseUnpublished
    from .deployment import DeploymentCreated as DeploymentCreated
    from .discussion import DiscussionCreated as DiscussionCreated
    from .discussion import DiscussionDeleted as DiscussionDeleted
    from .discussion import DiscussionLabeled as DiscussionLabeled
    from .membership import MembershipRemoved as MembershipRemoved
    from .project_card import ProjectCardMoved as ProjectCardMoved
    from .repository import RepositoryCreated as RepositoryCreated
    from .repository import RepositoryDeleted as RepositoryDeleted
    from .repository import RepositoryRenamed as RepositoryRenamed
    from .sponsorship import SponsorshipEdited as SponsorshipEdited
    from .discussion import DiscussionAnswered as DiscussionAnswered
    from .discussion import DiscussionReopened as DiscussionReopened
    from .discussion import DiscussionUnlocked as DiscussionUnlocked
    from .discussion import DiscussionUnpinned as DiscussionUnpinned
    from .project_card import ProjectCardEdited as ProjectCardEdited
    from .pull_request import PullRequestClosed as PullRequestClosed
    from .pull_request import PullRequestEdited as PullRequestEdited
    from .pull_request import PullRequestLocked as PullRequestLocked
    from .pull_request import PullRequestOpened as PullRequestOpened
    from .repository import RepositoryArchived as RepositoryArchived
    from .team import TeamAddedToRepository as TeamAddedToRepository
    from .workflow_job import WorkflowJobQueued as WorkflowJobQueued
    from .check_run import CheckRunRerequested as CheckRunRerequested
    from .sponsorship import SponsorshipCreated as SponsorshipCreated
    from .discussion import DiscussionUnlabeled as DiscussionUnlabeled
    from .project_card import ProjectCardCreated as ProjectCardCreated
    from .project_card import ProjectCardDeleted as ProjectCardDeleted
    from .pull_request import PullRequestLabeled as PullRequestLabeled
    from .workflow_job import WorkflowJobWaiting as WorkflowJobWaiting
    from .check_suite import CheckSuiteCompleted as CheckSuiteCompleted
    from .check_suite import CheckSuiteRequested as CheckSuiteRequested
    from .issue_comment import IssueCommentEdited as IssueCommentEdited
    from .merge_group import MergeGroupDestroyed as MergeGroupDestroyed
    from .repository_import import RepositoryImport as RepositoryImport
    from .workflow_dispatch import WorkflowDispatch as WorkflowDispatch
    from .discussion import DiscussionUnanswered as DiscussionUnanswered
    from .installation import InstallationCreated as InstallationCreated
    from .installation import InstallationDeleted as InstallationDeleted
    from .installation import InstallationSuspend as InstallationSuspend
    from .organization import OrganizationDeleted as OrganizationDeleted
    from .organization import OrganizationRenamed as OrganizationRenamed
    from .project_column import ProjectColumnMoved as ProjectColumnMoved
    from .pull_request import PullRequestAssigned as PullRequestAssigned
    from .pull_request import PullRequestDequeued as PullRequestDequeued
    from .pull_request import PullRequestEnqueued as PullRequestEnqueued
    from .pull_request import PullRequestReopened as PullRequestReopened
    from .pull_request import PullRequestUnlocked as PullRequestUnlocked
    from .repository import RepositoryPrivatized as RepositoryPrivatized
    from .repository import RepositoryPublicized as RepositoryPublicized
    from .repository import RepositoryUnarchived as RepositoryUnarchived
    from .issue_comment import IssueCommentCreated as IssueCommentCreated
    from .issue_comment import IssueCommentDeleted as IssueCommentDeleted
    from .sponsorship import SponsorshipCancelled as SponsorshipCancelled
    from .discussion import DiscussionTransferred as DiscussionTransferred
    from .project_card import ProjectCardConverted as ProjectCardConverted
    from .project_column import ProjectColumnEdited as ProjectColumnEdited
    from .pull_request import PullRequestUnlabeled as PullRequestUnlabeled
    from .repository import RepositoryTransferred as RepositoryTransferred
    from .workflow_job import WorkflowJobCompleted as WorkflowJobCompleted
    from .workflow_run import WorkflowRunCompleted as WorkflowRunCompleted
    from .workflow_run import WorkflowRunRequested as WorkflowRunRequested
    from .check_suite import CheckSuiteRerequested as CheckSuiteRerequested
    from .commit_comment import CommitCommentCreated as CommitCommentCreated
    from .installation import InstallationUnsuspend as InstallationUnsuspend
    from .project_column import ProjectColumnCreated as ProjectColumnCreated
    from .project_column import ProjectColumnDeleted as ProjectColumnDeleted
    from .pull_request import PullRequestMilestoned as PullRequestMilestoned
    from .pull_request import PullRequestUnassigned as PullRequestUnassigned
    from .team import TeamRemovedFromRepository as TeamRemovedFromRepository
    from .workflow_job import WorkflowJobInProgress as WorkflowJobInProgress
    from .workflow_run import WorkflowRunInProgress as WorkflowRunInProgress
    from .check_run import CheckRunRequestedAction as CheckRunRequestedAction
    from .sponsorship import SponsorshipTierChanged as SponsorshipTierChanged
    from .dependabot_alert import DependabotAlertFixed as DependabotAlertFixed
    from .projects_v2_item import ProjectsV2ItemEdited as ProjectsV2ItemEdited
    from .pull_request import PullRequestSynchronize as PullRequestSynchronize
    from .custom_property import CustomPropertyCreated as CustomPropertyCreated
    from .custom_property import CustomPropertyDeleted as CustomPropertyDeleted
    from .custom_property import CustomPropertyUpdated as CustomPropertyUpdated
    from .projects_v2 import ProjectsV2ProjectClosed as ProjectsV2ProjectClosed
    from .projects_v2 import ProjectsV2ProjectEdited as ProjectsV2ProjectEdited
    from .organization import OrganizationMemberAdded as OrganizationMemberAdded
    from .projects_v2_item import ProjectsV2ItemCreated as ProjectsV2ItemCreated
    from .projects_v2_item import ProjectsV2ItemDeleted as ProjectsV2ItemDeleted
    from .pull_request import PullRequestDemilestoned as PullRequestDemilestoned
    from .projects_v2 import ProjectsV2ProjectCreated as ProjectsV2ProjectCreated
    from .projects_v2 import ProjectsV2ProjectDeleted as ProjectsV2ProjectDeleted
    from .security_and_analysis import SecurityAndAnalysis as SecurityAndAnalysis
    from .dependabot_alert import DependabotAlertCreated as DependabotAlertCreated
    from .discussion import DiscussionCategoryChanged as DiscussionCategoryChanged
    from .projects_v2_item import ProjectsV2ItemArchived as ProjectsV2ItemArchived
    from .projects_v2_item import ProjectsV2ItemRestored as ProjectsV2ItemRestored
    from .registry_package import RegistryPackageUpdated as RegistryPackageUpdated
    from .merge_group import MergeGroupChecksRequested as MergeGroupChecksRequested
    from .projects_v2 import ProjectsV2ProjectReopened as ProjectsV2ProjectReopened
    from .dependabot_alert import DependabotAlertReopened as DependabotAlertReopened
    from .organization import OrganizationMemberInvited as OrganizationMemberInvited
    from .organization import OrganizationMemberRemoved as OrganizationMemberRemoved
    from .projects_v2_item import ProjectsV2ItemConverted as ProjectsV2ItemConverted
    from .projects_v2_item import ProjectsV2ItemReordered as ProjectsV2ItemReordered
    from .pull_request import PullRequestReadyForReview as PullRequestReadyForReview
    from .code_scanning_alert import CodeScanningAlertFixed as CodeScanningAlertFixed
    from .deployment_status import DeploymentStatusCreated as DeploymentStatusCreated
    from .security_advisory import SecurityAdvisoryUpdated as SecurityAdvisoryUpdated
    from .dependabot_alert import DependabotAlertDismissed as DependabotAlertDismissed
    from .discussion_comment import DiscussionCommentEdited as DiscussionCommentEdited
    from .pull_request import PullRequestReviewRequested as PullRequestReviewRequested
    from .registry_package import RegistryPackagePublished as RegistryPackagePublished
    from .repository_ruleset import RepositoryRulesetEdited as RepositoryRulesetEdited
    from .deployment_review import DeploymentReviewApproved as DeploymentReviewApproved
    from .deployment_review import DeploymentReviewRejected as DeploymentReviewRejected
    from .pull_request_review import PullRequestReviewEdited as PullRequestReviewEdited
    from .discussion_comment import DiscussionCommentCreated as DiscussionCommentCreated
    from .discussion_comment import DiscussionCommentDeleted as DiscussionCommentDeleted
    from .pull_request import PullRequestAutoMergeEnabled as PullRequestAutoMergeEnabled
    from .pull_request import PullRequestConvertedToDraft as PullRequestConvertedToDraft
    from .repository_ruleset import RepositoryRulesetCreated as RepositoryRulesetCreated
    from .repository_ruleset import RepositoryRulesetDeleted as RepositoryRulesetDeleted
    from .code_scanning_alert import (
        CodeScanningAlertCreated as CodeScanningAlertCreated,
    )
    from .deployment_review import (
        DeploymentReviewRequested as DeploymentReviewRequested,
    )
    from .repository_dispatch import (
        RepositoryDispatchSample as RepositoryDispatchSample,
    )
    from .security_advisory import (
        SecurityAdvisoryPublished as SecurityAdvisoryPublished,
    )
    from .security_advisory import (
        SecurityAdvisoryWithdrawn as SecurityAdvisoryWithdrawn,
    )
    from .sponsorship import (
        SponsorshipPendingTierChange as SponsorshipPendingTierChange,
    )
    from .pull_request import (
        PullRequestAutoMergeDisabled as PullRequestAutoMergeDisabled,
    )
    from .code_scanning_alert import (
        CodeScanningAlertReopened as CodeScanningAlertReopened,
    )
    from .installation_target import (
        InstallationTargetRenamed as InstallationTargetRenamed,
    )
    from .dependabot_alert import (
        DependabotAlertAutoReopened as DependabotAlertAutoReopened,
    )
    from .dependabot_alert import (
        DependabotAlertReintroduced as DependabotAlertReintroduced,
    )
    from .pull_request_review import (
        PullRequestReviewDismissed as PullRequestReviewDismissed,
    )
    from .pull_request_review import (
        PullRequestReviewSubmitted as PullRequestReviewSubmitted,
    )
    from .repository_advisory import (
        RepositoryAdvisoryReported as RepositoryAdvisoryReported,
    )
    from .sponsorship import (
        SponsorshipPendingCancellation as SponsorshipPendingCancellation,
    )
    from .dependabot_alert import (
        DependabotAlertAutoDismissed as DependabotAlertAutoDismissed,
    )
    from .marketplace_purchase import (
        MarketplacePurchaseChanged as MarketplacePurchaseChanged,
    )
    from .repository_advisory import (
        RepositoryAdvisoryPublished as RepositoryAdvisoryPublished,
    )
    from .secret_scanning_alert import (
        SecretScanningAlertCreated as SecretScanningAlertCreated,
    )
    from .secret_scanning_alert import (
        SecretScanningAlertRevoked as SecretScanningAlertRevoked,
    )
    from .branch_protection_rule import (
        BranchProtectionRuleEdited as BranchProtectionRuleEdited,
    )
    from .pull_request import (
        PullRequestReviewRequestRemoved as PullRequestReviewRequestRemoved,
    )
    from .secret_scanning_alert import (
        SecretScanningAlertReopened as SecretScanningAlertReopened,
    )
    from .secret_scanning_alert import (
        SecretScanningAlertResolved as SecretScanningAlertResolved,
    )
    from .branch_protection_rule import (
        BranchProtectionRuleCreated as BranchProtectionRuleCreated,
    )
    from .branch_protection_rule import (
        BranchProtectionRuleDeleted as BranchProtectionRuleDeleted,
    )
    from .custom_property_values import (
        CustomPropertyValuesUpdated as CustomPropertyValuesUpdated,
    )
    from .marketplace_purchase import (
        MarketplacePurchaseCancelled as MarketplacePurchaseCancelled,
    )
    from .marketplace_purchase import (
        MarketplacePurchasePurchased as MarketplacePurchasePurchased,
    )
    from .code_scanning_alert import (
        CodeScanningAlertClosedByUser as CodeScanningAlertClosedByUser,
    )
    from .installation import (
        InstallationNewPermissionsAccepted as InstallationNewPermissionsAccepted,
    )
    from .code_scanning_alert import (
        CodeScanningAlertReopenedByUser as CodeScanningAlertReopenedByUser,
    )
    from .github_app_authorization import (
        GithubAppAuthorizationRevoked as GithubAppAuthorizationRevoked,
    )
    from .installation_repositories import (
        InstallationRepositoriesAdded as InstallationRepositoriesAdded,
    )
    from .marketplace_purchase import (
        MarketplacePurchasePendingChange as MarketplacePurchasePendingChange,
    )
    from .code_scanning_alert import (
        CodeScanningAlertAppearedInBranch as CodeScanningAlertAppearedInBranch,
    )
    from .installation_repositories import (
        InstallationRepositoriesRemoved as InstallationRepositoriesRemoved,
    )
    from .pull_request_review_comment import (
        PullRequestReviewCommentEdited as PullRequestReviewCommentEdited,
    )
    from .pull_request_review_thread import (
        PullRequestReviewThreadResolved as PullRequestReviewThreadResolved,
    )
    from .pull_request_review_comment import (
        PullRequestReviewCommentCreated as PullRequestReviewCommentCreated,
    )
    from .pull_request_review_comment import (
        PullRequestReviewCommentDeleted as PullRequestReviewCommentDeleted,
    )
    from .deployment_protection_rule import (
        DeploymentProtectionRuleRequested as DeploymentProtectionRuleRequested,
    )
    from .pull_request_review_thread import (
        PullRequestReviewThreadUnresolved as PullRequestReviewThreadUnresolved,
    )
    from .personal_access_token_request import (
        PersonalAccessTokenRequestDenied as PersonalAccessTokenRequestDenied,
    )
    from .personal_access_token_request import (
        PersonalAccessTokenRequestCreated as PersonalAccessTokenRequestCreated,
    )
    from .personal_access_token_request import (
        PersonalAccessTokenRequestApproved as PersonalAccessTokenRequestApproved,
    )
    from .repository_vulnerability_alert import (
        RepositoryVulnerabilityAlertCreate as RepositoryVulnerabilityAlertCreate,
    )
    from .repository_vulnerability_alert import (
        RepositoryVulnerabilityAlertReopen as RepositoryVulnerabilityAlertReopen,
    )
    from .secret_scanning_alert_location import (
        SecretScanningAlertLocationCreated as SecretScanningAlertLocationCreated,
    )
    from .personal_access_token_request import (
        PersonalAccessTokenRequestCancelled as PersonalAccessTokenRequestCancelled,
    )
    from .repository_vulnerability_alert import (
        RepositoryVulnerabilityAlertDismiss as RepositoryVulnerabilityAlertDismiss,
    )
    from .repository_vulnerability_alert import (
        RepositoryVulnerabilityAlertResolve as RepositoryVulnerabilityAlertResolve,
    )
    from .marketplace_purchase import (
        MarketplacePurchasePendingChangeCancelled as MarketplacePurchasePendingChangeCancelled,
    )
    from .branch_protection_configuration import (
        BranchProtectionConfigurationEnabled as BranchProtectionConfigurationEnabled,
    )
    from .branch_protection_configuration import (
        BranchProtectionConfigurationDisabled as BranchProtectionConfigurationDisabled,
    )


else:
    __lazy_vars__ = {
        ".branch_protection_configuration": (
            "BranchProtectionConfigurationDisabled",
            "BranchProtectionConfigurationEnabled",
        ),
        ".branch_protection_rule": (
            "BranchProtectionRuleCreated",
            "BranchProtectionRuleDeleted",
            "BranchProtectionRuleEdited",
        ),
        ".check_run": (
            "CheckRunCompleted",
            "CheckRunCreated",
            "CheckRunRequestedAction",
            "CheckRunRerequested",
        ),
        ".check_suite": (
            "CheckSuiteCompleted",
            "CheckSuiteRequested",
            "CheckSuiteRerequested",
        ),
        ".code_scanning_alert": (
            "CodeScanningAlertAppearedInBranch",
            "CodeScanningAlertClosedByUser",
            "CodeScanningAlertCreated",
            "CodeScanningAlertFixed",
            "CodeScanningAlertReopened",
            "CodeScanningAlertReopenedByUser",
        ),
        ".commit_comment": ("CommitCommentCreated",),
        ".create": ("Create",),
        ".custom_property": (
            "CustomPropertyCreated",
            "CustomPropertyDeleted",
            "CustomPropertyUpdated",
        ),
        ".custom_property_values": ("CustomPropertyValuesUpdated",),
        ".delete": ("Delete",),
        ".dependabot_alert": (
            "DependabotAlertAutoDismissed",
            "DependabotAlertAutoReopened",
            "DependabotAlertCreated",
            "DependabotAlertDismissed",
            "DependabotAlertFixed",
            "DependabotAlertReintroduced",
            "DependabotAlertReopened",
        ),
        ".deploy_key": (
            "DeployKeyCreated",
            "DeployKeyDeleted",
        ),
        ".deployment": ("DeploymentCreated",),
        ".deployment_protection_rule": ("DeploymentProtectionRuleRequested",),
        ".deployment_review": (
            "DeploymentReviewApproved",
            "DeploymentReviewRejected",
            "DeploymentReviewRequested",
        ),
        ".deployment_status": ("DeploymentStatusCreated",),
        ".discussion": (
            "DiscussionAnswered",
            "DiscussionCategoryChanged",
            "DiscussionClosed",
            "DiscussionCreated",
            "DiscussionDeleted",
            "DiscussionEdited",
            "DiscussionLabeled",
            "DiscussionLocked",
            "DiscussionPinned",
            "DiscussionReopened",
            "DiscussionTransferred",
            "DiscussionUnanswered",
            "DiscussionUnlabeled",
            "DiscussionUnlocked",
            "DiscussionUnpinned",
        ),
        ".discussion_comment": (
            "DiscussionCommentCreated",
            "DiscussionCommentDeleted",
            "DiscussionCommentEdited",
        ),
        ".fork": ("Fork",),
        ".github_app_authorization": ("GithubAppAuthorizationRevoked",),
        ".gollum": ("Gollum",),
        ".installation": (
            "InstallationCreated",
            "InstallationDeleted",
            "InstallationNewPermissionsAccepted",
            "InstallationSuspend",
            "InstallationUnsuspend",
        ),
        ".installation_repositories": (
            "InstallationRepositoriesAdded",
            "InstallationRepositoriesRemoved",
        ),
        ".installation_target": ("InstallationTargetRenamed",),
        ".issue_comment": (
            "IssueCommentCreated",
            "IssueCommentDeleted",
            "IssueCommentEdited",
        ),
        ".issues": (
            "IssuesAssigned",
            "IssuesClosed",
            "IssuesDeleted",
            "IssuesDemilestoned",
            "IssuesEdited",
            "IssuesLabeled",
            "IssuesLocked",
            "IssuesMilestoned",
            "IssuesOpened",
            "IssuesPinned",
            "IssuesReopened",
            "IssuesTransferred",
            "IssuesUnassigned",
            "IssuesUnlabeled",
            "IssuesUnlocked",
            "IssuesUnpinned",
        ),
        ".label": (
            "LabelCreated",
            "LabelDeleted",
            "LabelEdited",
        ),
        ".marketplace_purchase": (
            "MarketplacePurchaseCancelled",
            "MarketplacePurchaseChanged",
            "MarketplacePurchasePendingChange",
            "MarketplacePurchasePendingChangeCancelled",
            "MarketplacePurchasePurchased",
        ),
        ".member": (
            "MemberAdded",
            "MemberEdited",
            "MemberRemoved",
        ),
        ".membership": (
            "MembershipAdded",
            "MembershipRemoved",
        ),
        ".merge_group": (
            "MergeGroupChecksRequested",
            "MergeGroupDestroyed",
        ),
        ".meta": ("MetaDeleted",),
        ".milestone": (
            "MilestoneClosed",
            "MilestoneCreated",
            "MilestoneDeleted",
            "MilestoneEdited",
            "MilestoneOpened",
        ),
        ".org_block": (
            "OrgBlockBlocked",
            "OrgBlockUnblocked",
        ),
        ".organization": (
            "OrganizationDeleted",
            "OrganizationMemberAdded",
            "OrganizationMemberInvited",
            "OrganizationMemberRemoved",
            "OrganizationRenamed",
        ),
        ".package": (
            "PackagePublished",
            "PackageUpdated",
        ),
        ".page_build": ("PageBuild",),
        ".personal_access_token_request": (
            "PersonalAccessTokenRequestApproved",
            "PersonalAccessTokenRequestCancelled",
            "PersonalAccessTokenRequestCreated",
            "PersonalAccessTokenRequestDenied",
        ),
        ".ping": ("Ping",),
        ".project_card": (
            "ProjectCardConverted",
            "ProjectCardCreated",
            "ProjectCardDeleted",
            "ProjectCardEdited",
            "ProjectCardMoved",
        ),
        ".project": (
            "ProjectClosed",
            "ProjectCreated",
            "ProjectDeleted",
            "ProjectEdited",
            "ProjectReopened",
        ),
        ".project_column": (
            "ProjectColumnCreated",
            "ProjectColumnDeleted",
            "ProjectColumnEdited",
            "ProjectColumnMoved",
        ),
        ".projects_v2": (
            "ProjectsV2ProjectClosed",
            "ProjectsV2ProjectCreated",
            "ProjectsV2ProjectDeleted",
            "ProjectsV2ProjectEdited",
            "ProjectsV2ProjectReopened",
        ),
        ".projects_v2_item": (
            "ProjectsV2ItemArchived",
            "ProjectsV2ItemConverted",
            "ProjectsV2ItemCreated",
            "ProjectsV2ItemDeleted",
            "ProjectsV2ItemEdited",
            "ProjectsV2ItemReordered",
            "ProjectsV2ItemRestored",
        ),
        ".public": ("Public",),
        ".pull_request": (
            "PullRequestAssigned",
            "PullRequestAutoMergeDisabled",
            "PullRequestAutoMergeEnabled",
            "PullRequestClosed",
            "PullRequestConvertedToDraft",
            "PullRequestDemilestoned",
            "PullRequestDequeued",
            "PullRequestEdited",
            "PullRequestEnqueued",
            "PullRequestLabeled",
            "PullRequestLocked",
            "PullRequestMilestoned",
            "PullRequestOpened",
            "PullRequestReadyForReview",
            "PullRequestReopened",
            "PullRequestReviewRequestRemoved",
            "PullRequestReviewRequested",
            "PullRequestSynchronize",
            "PullRequestUnassigned",
            "PullRequestUnlabeled",
            "PullRequestUnlocked",
        ),
        ".pull_request_review_comment": (
            "PullRequestReviewCommentCreated",
            "PullRequestReviewCommentDeleted",
            "PullRequestReviewCommentEdited",
        ),
        ".pull_request_review": (
            "PullRequestReviewDismissed",
            "PullRequestReviewEdited",
            "PullRequestReviewSubmitted",
        ),
        ".pull_request_review_thread": (
            "PullRequestReviewThreadResolved",
            "PullRequestReviewThreadUnresolved",
        ),
        ".push": ("Push",),
        ".registry_package": (
            "RegistryPackagePublished",
            "RegistryPackageUpdated",
        ),
        ".release": (
            "ReleaseCreated",
            "ReleaseDeleted",
            "ReleaseEdited",
            "ReleasePrereleased",
            "ReleasePublished",
            "ReleaseReleased",
            "ReleaseUnpublished",
        ),
        ".repository_advisory": (
            "RepositoryAdvisoryPublished",
            "RepositoryAdvisoryReported",
        ),
        ".repository": (
            "RepositoryArchived",
            "RepositoryCreated",
            "RepositoryDeleted",
            "RepositoryEdited",
            "RepositoryPrivatized",
            "RepositoryPublicized",
            "RepositoryRenamed",
            "RepositoryTransferred",
            "RepositoryUnarchived",
        ),
        ".repository_dispatch": ("RepositoryDispatchSample",),
        ".repository_import": ("RepositoryImport",),
        ".repository_ruleset": (
            "RepositoryRulesetCreated",
            "RepositoryRulesetDeleted",
            "RepositoryRulesetEdited",
        ),
        ".repository_vulnerability_alert": (
            "RepositoryVulnerabilityAlertCreate",
            "RepositoryVulnerabilityAlertDismiss",
            "RepositoryVulnerabilityAlertReopen",
            "RepositoryVulnerabilityAlertResolve",
        ),
        ".secret_scanning_alert": (
            "SecretScanningAlertCreated",
            "SecretScanningAlertReopened",
            "SecretScanningAlertResolved",
            "SecretScanningAlertRevoked",
        ),
        ".secret_scanning_alert_location": ("SecretScanningAlertLocationCreated",),
        ".security_advisory": (
            "SecurityAdvisoryPublished",
            "SecurityAdvisoryUpdated",
            "SecurityAdvisoryWithdrawn",
        ),
        ".security_and_analysis": ("SecurityAndAnalysis",),
        ".sponsorship": (
            "SponsorshipCancelled",
            "SponsorshipCreated",
            "SponsorshipEdited",
            "SponsorshipPendingCancellation",
            "SponsorshipPendingTierChange",
            "SponsorshipTierChanged",
        ),
        ".star": (
            "StarCreated",
            "StarDeleted",
        ),
        ".status": ("Status",),
        ".team_add": ("TeamAdd",),
        ".team": (
            "TeamAddedToRepository",
            "TeamCreated",
            "TeamDeleted",
            "TeamEdited",
            "TeamRemovedFromRepository",
        ),
        ".watch": ("WatchStarted",),
        ".workflow_dispatch": ("WorkflowDispatch",),
        ".workflow_job": (
            "WorkflowJobCompleted",
            "WorkflowJobInProgress",
            "WorkflowJobQueued",
            "WorkflowJobWaiting",
        ),
        ".workflow_run": (
            "WorkflowRunCompleted",
            "WorkflowRunInProgress",
            "WorkflowRunRequested",
        ),
        "._base": ("Event",),
        "._types": ("events",),
    }
