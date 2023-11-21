'''In pytest, the conftest.py file is a powerful mechanism for sharing fixtures, configurations, and hooks 
across multiple test files or directories within a project. This file serves as a central location to define 
fixtures and other configurations that can be used by multiple test modules.

Key points about conftest.py:

1. Fixture Sharing: Fixtures defined in conftest.py can be automatically discovered and used by multiple test 
iles without explicit imports. This means you can define fixtures once in conftest.py, and they become 
available to all tests in the same directory and subdirectories.

2. Scope of Fixtures: Fixtures defined in conftest.py follow a scope that depends on where conftest.py is 
located. Fixtures in the conftest.py file of a specific directory apply to the tests in that directory and 
its subdirectories.

3. Configuration and Hooks: Besides fixtures, conftest.py can contain configurations, hooks, and other 
pytest-related settings that affect the test run or modify pytest's behavior.

4. Directory Structure: Typically, conftest.py should be placed at the root of a test directory or at 
higher levels within the project directory structure to provide fixtures and configurations that can be 
shared across multiple test files.'''

# project/
# ├── conftest.py
# ├── tests/
# │   ├── test_module1.py
# │   ├── test_module2.py
# │   └── subdirectory/
# │       ├── test_module3.py
# │       └── conftest.py

'''In this structure, conftest.py at the root level provides fixtures and configurations for all the test 
files in the tests/ directory and its subdirectories. The conftest.py file within the subdirectory/ affects 
only the test files within that subdirectory and its subdirectories.

conftest.py is a powerful tool for organizing and centralizing setup, teardown, and configuration for pytest 
tests, enhancing code reuse and maintainability across a test suite.'''


import pytest


@pytest.fixture()
# This base fixtue will be present to all the files the directory
def base():
    print("I will run first")
    yield
    print("I will run last")

