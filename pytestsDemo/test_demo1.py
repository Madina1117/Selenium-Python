# any pytest file should start with "test_" keyword or end with _test
# pytest method names should start with "test"
# any code should be wrapped in method

import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello!")


@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good morning!")


def test_crossBrowser(crossBrowser):
    print(crossBrowser)