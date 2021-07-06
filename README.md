

# main-entry


[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]
[![Code Coverage][coverage-image]][coverage-url]
[![Code Quality][quality-image]][quality-url]

[pypi-image]: https://img.shields.io/pypi/v/podsearch
[pypi-url]: https://pypi.org/project/mainentry/
[build-image]: https://github.com/fanoway/main-entry/actions/workflows/build.yml/badge.svg
[build-url]: https://github.com/fanoway/main-entry/actions/workflows/build.yml
[coverage-image]: https://codecov.io/gh/fanoway/main-entry/branch/main/graph/badge.svg
[coverage-url]: https://codecov.io/gh/fanoway/main-entry
[quality-image]: https://api.codeclimate.com/v1/badges/3130fa0ba3b7993fbf0a/maintainability
[quality-url]: https://codeclimate.com/github/fanoway/main-entry

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


