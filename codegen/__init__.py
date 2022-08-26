import inspect
from pathlib import Path
from itertools import chain
from dataclasses import dataclass
from typing import Dict, List, Union, get_args, get_origin

from jinja2 import Environment, PackageLoader
from githubkit.webhooks.models import GitHubWebhookModel
from githubkit.webhooks.types import webhook_action_types

MESSAGE_EVENTS = {
    "CommitCommentCreated",
    "IssueCommentCreated",
    "PullRequestReviewCommentCreated",
}
HAS_MESSAGE_EVENTS = {
    "CommitCommentCreated",
    "IssueCommentCreated",
    "IssueCommentDeleted",
    "IssueCommentEdited",
    "PullRequestReviewCommentCreated",
    "PullRequestReviewCommentDeleted",
    "PullRequestReviewCommentEdited",
}


@dataclass
class Data:
    class_name: str
    payload_type: str


def pascal_case(*names: str) -> str:
    words = chain.from_iterable(name.split("_") for name in names)
    return "".join(word if word.isupper() else word.capitalize() for word in words)


def build_event():
    imports: List[str] = []
    events: List[Data] = []
    event_types: Dict[str, Union[str, Dict[str, str]]] = {}
    for event, types in webhook_action_types.items():
        if not isinstance(types, dict):
            imports.append(f"{types.__name__} as {types.__name__}Payload")
            events.append(Data(types.__name__, f"{types.__name__}Payload"))
            event_types[event] = types.__name__
            continue

        action_types: Dict[str, str] = {}
        event_types[event] = action_types
        for action, type in types.items():
            if inspect.isclass(type) and issubclass(type, GitHubWebhookModel):
                imports.append(f"{type.__name__} as {type.__name__}Payload")
                events.append(Data(type.__name__, f"{type.__name__}Payload"))
                action_types[action] = type.__name__
            else:
                assert get_origin(type) is Union
                imports.extend(model.__name__ for model in get_args(type))
                events.append(
                    Data(
                        pascal_case(event, action),
                        f"Union[{', '.join(model.__name__ for model in get_args(type))}]",
                    )
                )
                action_types[action] = pascal_case(event, action)

    env = Environment(loader=PackageLoader("codegen"))
    template = env.get_template("event.py.jinja")
    event_text = template.render(
        imports=imports,
        events=events,
        types=event_types,
        message_events=MESSAGE_EVENTS,
        has_message_events=HAS_MESSAGE_EVENTS,
    )
    Path("./nonebot/adapters/github/event.py").write_text(event_text)
