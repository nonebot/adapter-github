from githubkit.versions.latest.models import WebhookDiscussionTransferred

from ._base import Event


class DiscussionTransferred(Event):

    payload: WebhookDiscussionTransferred
