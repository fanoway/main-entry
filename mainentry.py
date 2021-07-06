"""Wrapper to replace if __name__ == "__main__": with a more pythonic decorator"""


__version__ = "1.00"

import inspect


def entry(func):
    def wrapper():
        if inspect.stack()[1].frame.f_locals.get("__name__") == "__main__":
            func()

    return wrapper
