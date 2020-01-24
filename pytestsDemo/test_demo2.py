# any pytest file should start with "test_" keyword or end with _test
# pytest method names should start with "test"
# any code should be wrapped in method
# method name should have sense
# -k stands for method names execution, -s for logs in output, -v stands for more info metadata
# you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run -m option
# you can skip tests with @pytest.mark.skip
# @pytest.mark.xfail
# fixtures are used for as setup and tear down methods for test cases - conftest file to generalize fixture
# and make it available to all test cases
# data driven and parametrization can be done with return statement in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings don't match"


def test_secondCreditCard():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition does not match"


@pytest.fixture()
def setup():
    print("I will be executed first")


def testFixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")