from githubkit.versions.latest.models import WebhookPageBuild

from ._base import Event


class PageBuild(Event):

    payload: WebhookPageBuild
