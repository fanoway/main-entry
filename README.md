# main-entry

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Simple wrapper to replace `if __name__ = "__main__":` with a nice clean `@entry` wrapper

## Installation

main-entry can be installed using pip and has no dependancies

```
pip install mainentry
```

## Usage

```python
from mainentry import entry


@entry
def helloworld():
    # Use this as your primary function
    print("Hello World")


# Call primary function
helloworld()


```


