from githubkit.versions.latest.models import WebhookDiscussionUnlabeled

from ._base import Event


class DiscussionUnlabeled(Event):

    payload: WebhookDiscussionUnlabeled
