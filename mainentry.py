"""Wrapper to replace if __name__ == "__main__": with a decorator"""


__version__ = "1.01"

import inspect


def entry(func):
    """decorator"""

    def wrapper():
        """__name__ check"""
        if inspect.stack()[1].frame.f_locals.get("__name__") == "__main__":
            func()

    return wrapper
