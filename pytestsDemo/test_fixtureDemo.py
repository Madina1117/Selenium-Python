import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def testFixtureDemo(self):
        print("I will execute steps in fixtureDemo method")  # when declaring any method in class, mandatory param is self

    def testFixtureDemo1(self):
        print("I will execute steps in fixtureDemo1 method")

    def testFixtureDemo2(self):
        print("I will execute steps in fixtureDemo2 method")

    def testFixtureDemo3(self):
        print("I will execute steps in fixtureDemo3 method")


