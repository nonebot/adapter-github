from dataclasses import dataclass
import inspect
from itertools import chain
from pathlib import Path
import shutil
from typing import Union, cast
from typing_extensions import get_args, get_origin

from githubkit import GitHubModel
from githubkit.versions.latest.webhooks import webhook_action_types
from jinja2 import Environment, PackageLoader

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
    action: str | None
    class_name: str
    payload_types: list[str]


def module_name(event: str, action: Data) -> str:
    return f"{event}_{action.action}" if action.action else event


def pascal_case(*names: str) -> str:
    words = chain.from_iterable(name.split("_") for name in names)
    return "".join(word if word.isupper() else word.capitalize() for word in words)


def build_event():
    event_types: dict[str, list[Data]] = {}
    for event, types in webhook_action_types.items():
        # event has no sub action
        if not isinstance(types, dict):
            types = cast(type[GitHubModel], types)
            event_types[event] = [
                Data(
                    None,
                    types.__name__.removeprefix("Webhook"),
                    [types.__name__],
                )
            ]
            continue

        action_types: list[Data] = []
        event_types[event] = action_types
        for action, model in types.items():
            # action type is a simple model
            if inspect.isclass(model) and issubclass(model, GitHubModel):
                action_types.append(
                    Data(
                        action, model.__name__.removeprefix("Webhook"), [model.__name__]
                    )
                )
            # action type is a union of models
            else:
                assert get_origin(model) is Union
                action_types.append(
                    Data(
                        action,
                        pascal_case(event, action),
                        [model.__name__ for model in get_args(model)],
                    )
                )

    output_dir = Path("./nonebot/adapters/github/event/")

    if output_dir.exists():
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    env = Environment(loader=PackageLoader("codegen"))
    env.globals["filename"] = module_name

    # generate base model
    template = env.get_template("_base.py.jinja")
    base_text = template.render()
    (output_dir / "_base.py").write_text(base_text)

    # generate types
    template = env.get_template("_types.py.jinja")
    types_text = template.render(types=event_types)
    (output_dir / "_types.py").write_text(types_text)

    # generate event models
    template = env.get_template("event.py.jinja")
    for event, actions in event_types.items():
        for action in actions:
            event_text = template.render(
                action=action,
                message_events=MESSAGE_EVENTS,
                has_message_events=HAS_MESSAGE_EVENTS,
            )
            (output_dir / f"{module_name(event, action)}.py").write_text(event_text)

    # generate init file
    template = env.get_template("__init__.py.jinja")
    init_text = template.render(types=event_types)
    (output_dir / "__init__.py").write_text(init_text)
