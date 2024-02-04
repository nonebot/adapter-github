from githubkit.versions.latest.models import WebhookDiscussionCategoryChanged

from ._base import Event


class DiscussionCategoryChanged(Event):

    payload: WebhookDiscussionCategoryChanged
