"""Wrapper to replace if __name__ == "__main__": with a decorator"""


__version__ = "1.3"

import inspect
from typing import Any, TypeVar, Callable

F = TypeVar('F', bound=Callable[..., Any])

def entry(func: F) -> F:
    """decorator"""

    def wrapper():
        """__name__ check"""
        if inspect.stack()[1].frame.f_locals.get("__name__") == "__main__":
            func()

    return wrapper
