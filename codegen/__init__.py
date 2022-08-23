from typing import List
from dataclasses import dataclass

from githubkit.webhooks.types import webhook_action_types


@dataclass
class Data:
    class_name: str
    payload_type: str


def build_event():
    events: List[Data] = []
    for event, types in webhook_action_types.items():
        if not isinstance(types, dict):
            events.append(Data(types.__name__, types.__name__))

        for action, type in types.items():
            ...
