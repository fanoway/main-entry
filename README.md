#EntryPoint

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Simple wrapper to replace `if __name__ = "__main__":` with a nice clean `@main` wrapper

```python
from entrypoint import main

@main
def helloworld():
  print('Hello World')

```
