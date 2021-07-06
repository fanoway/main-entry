"""Wrapper to replace if __name__ == "__main__": as an entrypoint"""


__version__ = "0.1"


def main(func):
    def wrapper():
        if __name__ == "__main__":
            func()

    return wrapper
