from githubkit.versions.latest.models import WebhookDiscussionReopened

from ._base import Event


class DiscussionReopened(Event):

    payload: WebhookDiscussionReopened
