from githubkit.versions.latest.models import WebhookGollum

from ._base import Event


class Gollum(Event):

    payload: WebhookGollum
