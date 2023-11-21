
# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method names execution, -s logs in out put -v stands for more info like metadata
# we can run specific file with py.test command
# we can mark (tag) tests @pytest.mark.smoke and then run with -m 
# we can skip tests with @pytest.mark.skip
# @pytest.mark.xfail to not show ouput
import pytest

# @pytest.mark.smoke
# def test_method():
#     print("Hello")


def test_method2(base):
    print("good morning")