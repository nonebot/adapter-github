from typing import Optional

from pydantic import Extra, BaseModel


class Config(BaseModel, extra=Extra.ignore):
    """GitHub 配置类。"""

    webhook_secret: Optional[str] = None
    """GitHub Webhook Secret。默认不进行校验。"""
