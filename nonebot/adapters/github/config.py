from typing import Any, List, Union, Optional

from pydantic import Field, BaseModel

from .compat import field_validator


class OAuthApp(BaseModel):
    client_id: str
    client_secret: str
    webhook_secret: Optional[str] = None

    @property
    def id(self) -> str:
        return self.client_id


class GitHubApp(BaseModel):
    app_id: str
    private_key: str
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    webhook_secret: Optional[str] = None

    @property
    def id(self) -> str:
        return self.app_id

    @field_validator("private_key", mode="before")
    @classmethod
    def concat_key(cls, value: object) -> Any:
        return "\n".join(value) if isinstance(value, list) else value


class Config(BaseModel):
    """GitHub Adapter Config"""

    github_apps: List[Union[GitHubApp, OAuthApp]] = Field(default_factory=list)
    """Allowed GitHub App List"""
    github_base_url: Optional[str] = None
    github_accept_format: Optional[str] = None
    github_previews: Optional[List[str]] = None
