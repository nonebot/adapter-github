from typing import Type, Iterable
from typing_extensions import override

from nonebot.adapters import Message as BaseMessage
from nonebot.adapters import MessageSegment as BaseMessageSegment


class MessageSegment(BaseMessageSegment["Message"]):
    @classmethod
    @override
    def get_message_class(cls) -> Type["Message"]:
        return Message

    @override
    def __str__(self) -> str:
        if self.type == "markdown":
            return self.data["text"]
        return f"<{self.type}:{','.join(f'{k}={v}' for k, v in self.data.items())}>"

    @override
    def is_text(self) -> bool:
        return self.type == "markdown"

    @staticmethod
    def markdown(text: str) -> "MessageSegment":
        return MessageSegment("markdown", {"text": text})


class Message(BaseMessage[MessageSegment]):
    @classmethod
    @override
    def get_segment_class(cls) -> Type[MessageSegment]:
        return MessageSegment

    @staticmethod
    @override
    def _construct(msg: str) -> Iterable[MessageSegment]:
        yield MessageSegment.markdown(msg)
