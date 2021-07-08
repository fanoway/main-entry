"""Wrapper to replace if __name__ == "__main__": with a decorator"""

__version__ = "v2.0"

from .mainentry import entry

__all__ = ["entry"]
