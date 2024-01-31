from typing import Any, Dict
from typing_extensions import override

from nonebot.utils import escape_tag

from nonebot.adapters import Event as BaseEvent

from ..message import Message
from ..utils import get_attr_or_item


class Event(BaseEvent):
    id: str
    name: str
    payload: Dict[str, Any]

    to_me: bool = False

    @override
    def get_type(self) -> str:
        return "notice"

    @override
    def get_event_name(self) -> str:
        return self.name + (
            f".{action}" if (action := get_attr_or_item(self.payload, "action")) else ""
        )

    @override
    def get_event_description(self) -> str:
        return escape_tag(
            f"{self.__class__.__name__} {self.id}"
            + (
                f" from sender {sender_name}"
                if (sender := get_attr_or_item(self.payload, "sender"))
                and (sender_name := get_attr_or_item(sender, "login"))
                else ""
            )
            + (
                f" in repository {repo_name}"
                if (repo := get_attr_or_item(self.payload, "repository"))
                and (repo_name := get_attr_or_item(repo, "full_name"))
                else ""
            )
        )

    @override
    def get_message(self) -> Message:
        raise ValueError("Event has no message!")

    @override
    def get_user_id(self) -> str:
        if sender := get_attr_or_item(self.payload, "sender"):
            return sender.login
        raise ValueError("Event has no context!")

    @override
    def get_session_id(self) -> str:
        return self.get_user_id()

    @override
    def is_tome(self) -> bool:
        return self.to_me
