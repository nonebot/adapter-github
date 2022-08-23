import re

from nonebot.utils import logger_wrapper

log = logger_wrapper("GitHub")


def escape(content: str) -> str:
    return re.sub(r"\\|`|\*|_|{|}|\[|\]|\(|\)|#|\+|-|\.|!", r"\\\1", content)
