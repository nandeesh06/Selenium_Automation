'''Fixtures in pytest are functions that provide a baseline for your tests by 
setting up preconditions or initializing resources needed for test functions to run.
 They allow you to organize and manage the setup and teardown logic for your tests.

Fixtures perform tasks like creating database connections, setting up test data, 
initializing objects, or performing any necessary preparations before running test functions. 
They help in keeping the test code clean, reusable, and well-structured.'''

import pytest


@pytest.fixture()
def base():
    print("I will run first")
    yield
    print("I will run last")

def test_ex_fix(base):
    print("I'm the main function")
