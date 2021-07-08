""" substitute for if __name__ == "__main__": """

import inspect
from typing import Any, TypeVar, Callable, cast

F = TypeVar("F", bound=Callable[..., Any])  # pylint: disable = invalid-name


def entry(func: F) -> F:
    """decorator"""

    def wrapper():
        """__name__ check"""
        if inspect.stack()[1].frame.f_locals.get("__name__") == "__main__":
            func()

    return cast(F, wrapper)
