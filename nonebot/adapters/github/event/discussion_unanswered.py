from githubkit.versions.latest.models import WebhookDiscussionUnanswered

from ._base import Event


class DiscussionUnanswered(Event):

    payload: WebhookDiscussionUnanswered
