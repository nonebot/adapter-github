from githubkit.versions.latest.models import WebhookDiscussionAnswered

from ._base import Event


class DiscussionAnswered(Event):

    payload: WebhookDiscussionAnswered
