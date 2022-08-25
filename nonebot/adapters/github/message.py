from typing import Type, Iterable

from nonebot.typing import overrides

from nonebot.adapters import Message as BaseMessage
from nonebot.adapters import MessageSegment as BaseMessageSegment


class MessageSegment(BaseMessageSegment["Message"]):
    @classmethod
    @overrides(BaseMessageSegment)
    def get_message_class(cls) -> Type["Message"]:
        return Message

    @overrides(BaseMessageSegment)
    def __str__(self) -> str:
        if self.type == "markdown":
            return self.data["text"]
        return f"<{self.type}:{','.join(f'{k}={v}' for k, v in self.data.items())}>"

    @overrides(BaseMessageSegment)
    def is_text(self) -> bool:
        return self.type == "markdown"

    @staticmethod
    def markdown(text: str) -> "MessageSegment":
        return MessageSegment("markdown", {"text": text})


class Message(BaseMessage[MessageSegment]):
    @classmethod
    @overrides(BaseMessage)
    def get_segment_class(cls) -> Type[MessageSegment]:
        return MessageSegment

    @staticmethod
    @overrides(BaseMessage)
    def _construct(msg: str) -> Iterable[MessageSegment]:
        yield MessageSegment.markdown(msg)
