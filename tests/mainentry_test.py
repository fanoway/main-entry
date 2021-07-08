import os
import runpy
import sys

from mainentry import entry

# add dummy module to sys.path
sys.path.append("./tests")
sys.path.insert(0, os.path.abspath(".."))

print(sys.path)


def test_notmain(capfd):
    # When running importing nothing should be written to the console by helloworld
    runpy.run_module("dummy_module", run_name="__notmain__")

    out, err = capfd.readouterr()
    assert out == ""


def test_ismain(capfd):
    # When running the moduel as name "Hello World" should be written to the console

    runpy.run_module("dummy_module", run_name="__main__")

    out, err = capfd.readouterr()
    assert out == "Hello World\n"
