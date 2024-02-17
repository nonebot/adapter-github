from typing import Literal

from nonebot.compat import PYDANTIC_V2

__all__ = ("field_validator",)

if PYDANTIC_V2:
    from pydantic import field_validator as field_validator
else:
    from pydantic import validator

    def field_validator(
        __field: str, *fields: str, mode: Literal["before", "after"] = "after"
    ):
        return validator(__field, *fields, pre=mode == "before", allow_reuse=True)
