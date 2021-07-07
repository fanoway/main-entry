from mainentry import entry
import runpy
import sys

# add dummy module to sys.path
sys.path.append("./tests")

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
