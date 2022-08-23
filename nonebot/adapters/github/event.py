from typing import Any

from nonebot.typing import overrides

from nonebot.adapters import Event as BaseEvent


class Event(BaseEvent):
    id: str
    name: str
    payload: Any
