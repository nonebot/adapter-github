from typing import List, Union, Optional

from pydantic import Extra, Field, BaseModel


class OAuthApp(BaseModel):
    client_id: str
    client_secret: str
    webhook_secret: Optional[str] = None


class GitHubApp(BaseModel):
    app_id: str
    private_key: str
    webhook_secret: Optional[str] = None


class Config(BaseModel, extra=Extra.ignore):
    """GitHub Adapter Config"""

    github_apps: List[Union[OAuthApp, GitHubApp]] = Field(default_factory=list)
    """Allowed GitHub App List。"""
