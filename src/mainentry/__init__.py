"""Wrapper to replace if __name__ == "__main__": with a decorator"""

__version__ = "1.3"

from .mainentry import entry

__all__ = ["entry"]
