from nonebot.typing import overrides

from nonebot.adapters import Event as BaseEvent


class Event(BaseEvent):
    event_id: str
    event_name: str
