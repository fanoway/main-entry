

# main-entry


[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![build](https://github.com/fanoway/main-entry/actions/workflows/build.yaml/badge.svg?branch=main)](https://github.com/fanoway/main-entry/actions/workflows/build.yaml)
[![codecov](https://codecov.io/gh/fanoway/main-entry/branch/main/graph/badge.svg?token=D3X4DZVA63)](https://codecov.io/gh/fanoway/main-entry)
[![Maintainability](https://api.codeclimate.com/v1/badges/49aeb04337c28d1b1016/maintainability)](https://codeclimate.com/github/fanoway/main-entry/maintainability)
[![PyPI version](https://badge.fury.io/py/mainentry.svg)](https://badge.fury.io/py/mainentry)



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


