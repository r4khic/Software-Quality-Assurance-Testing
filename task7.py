import pytest

'''Implement TestNG annotations'''


# Setup and Teardown for methods
@pytest.fixture
def setup_teardown():
    print("\nSetting up the test...")
    yield
    print("\nTearing down the test...")


# Setup and Teardown for class
@pytest.fixture(scope="class")
def setup_teardown_class():
    print("\nSetting up the CLASS...")
    yield
    print("\nTearing down the CLASS...")


# Individual tests with method-level setup and teardown
def test_example1(setup_teardown):
    print("Executing test_example1")


def test_example2(setup_teardown):
    print("Executing test_example2")


# Tests inside a class with class-level setup and teardown
@pytest.mark.usefixtures("setup_teardown_class")
class TestExample:

    def test_example1_in_class(self):
        print("Executing test_example1 inside class")

    def test_example2_in_class(self):
        print("Executing test_example2 inside class")


# Group-like tests using markers
@pytest.mark.regression
def test_regression_example():
    print("Executing regression test")


@pytest.mark.smoke
def test_smoke_example():
    print("Executing smoke test")
