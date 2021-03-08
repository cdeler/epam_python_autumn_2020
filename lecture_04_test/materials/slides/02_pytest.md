## Testing with python
There is 2 major tools for testing `unittest` and `pytest`.

De facto pytest is a standard in Python testing. `pytest` can do everything what can do unittest and even more.

### Unittest vs pytest
- pytest asserts are more informative
- pytest does not require writing test classes
- pytest fixtures are more flexible that setUp and tearDown
- pytest has plugins
- pytest is more widely used

## pytest: helps you write better programs
The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries

## Test runner

**pytest** will run all files of the form `test_*.py` or `*_test.py` in the current directory and its subdirectories. 

More generally, it follows standard test discovery rules.  


## pytest fixtures: explicit, modular, scalable
fixture - prepared data for test.

We will look into:

- creating fixture
- scope
- nested
- builtin fixtures
- tear down
- autouse

## How to create fixture

- Write a function
- Decorate with `@pytest.fixture()`
- Pass as argument to tests
- **pytest** will do it's magic


```python
import pytest


@pytest.fixture()
def smtp_connection():
    import smtplib

    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert 0  # for demo purposes
```

## What pytest do after you run it

- Collect fixtures
- Collect tests
- Execute fixtures required for test
- Run tests and pass result of fixture execution to it 
- Show reports

## Fixture scopes
You can shoose how often fixture is executed

- `function` (default, recommended), every time before test
- `class`, once for each test in class
- `module`, once for each test in module
- `package`, once for each test in package
- `session`, once per test execution

Use `function` everywhere and other to improve performance.

```python
# content of conftest.py
import pytest
import smtplib


@pytest.fixture(scope="module")
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
```


## Reuse fixture in the fixture (fixture in a fixture)

You can pass fixture not only in test, but also in another fixture.

```python
import pytest


@pytest.fixture
def john():
    return "John"

@pytest.fixture
def user_john(name):
    return User(name)
```

## Built-in fixtures

- caplog Control logging and access log entries.
- capsys Capture, as text, output to sys.stdout and sys.stderr.
- monkeypatch Temporarily modify classes, functions, dictionaries, os.environ, and other objects.
- pytestconfig Access to configuration values, pluginmanager and plugin hooks.
- request Provide information on the executing test function.
- testdir Provide a temporary test directory to aid in running, and testing, pytest plugins.
- tmp_path Provide a pathlib.Path object to a temporary directory which is unique to each test function.
- [and others](https://docs.pytest.org/en/stable/fixture.html)

## monkeypatch

Modify your environment to before the test, get it cleaned after automatically.

- monkeypatch.setattr(obj, name, value, raising=True)
- monkeypatch.delattr(obj, name, raising=True)
- monkeypatch.setitem(mapping, name, value)
- monkeypatch.delitem(obj, name, raising=True)
- monkeypatch.setenv(name, value, prepend=False)
- monkeypatch.delenv(name, raising=True)
- monkeypatch.syspath_prepend(path)
- monkeypatch.chdir(path)

```python
import sys


def foo():
    return 1


def boo(x):
    return x + foo()


def test_boo_with_monkeypatch(monkeypatch):
    this_module = sys.modules[__name__]
    monkeypatch.setattr(this_module, "foo", lambda: 2)
    assert boo(1) == 3


def test_boo(monkeypatch):
    assert boo(1) == 2
```

## Fixture instead of setUp and tearDown

`setUp` and `tearDown` are special methods executed before each test and after each test

```python
import pytest


@pytest.fixture
def connection():
    con = get_connection()
    yield con
    con.close()
```


## Use fixture without adding argument

```python
# content of test_setenv.py
import os
import pytest


@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit:
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile", "w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
```

## Run before any test

```python
@pytest.fixture(autouse=True)
def a1():
    order.append("a1")
```

## Test generation

```python
import pytest


@pytest.mark.parametrize("color", ["red", "green"])
@pytest.mark.parametrize("shape", ["box", "circle"])
def test_shape(shape, color):
    assert True
```

```
test/test_example.py::test_shape[box-red] PASSED                                                                         
test/test_example.py::test_shape[box-green] PASSED                                                                       
test/test_example.py::test_shape[circle-red] PASSED                                                               
test/test_example.py::test_shape[circle-green] PASSED   
```

## Do not overuse this feature

Please avoid putting all test in a single function.
You save some lines, but you hide meaning of the test.

Usually it is better to write separate function for each case you are testing: positive, negative, empty

### bad
All in one, you don't help reader to understand cases behind this inputs. 

```python
@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([0, 1, 1, 2], True),
        ([], False),
        ([0], False),
        ([0, 1, 1, 3], False),
        ([1, 1, 2], False),
    ],
)
def test_check_fibonacci(value: Sequence[int], expected_result: bool):
    actual_result = check_fibonacci(value)

    assert actual_result == expected_result
```

### good
```python

@pytest.mark.parametrize(
    "value",
    [
        [0, 1, 1, 2]

    ],
)
def test_sequence_is_fibonacci(value: Sequence[int]):
    assert check_fibonacci(value) is True


@pytest.mark.parametrize(
    "value",
    [
        [0],
        [0, 1, 1, 3],
        [1, 1, 2],
    ],
)
def test_sequence_is_not_fibonacci(value: Sequence[int]):
    assert check_fibonacci(value) is False

    
def test_empty_sequence_is_fibonacci():
    assert check_fibonacci([]) is False
```

## conftest.py

- stores fixtures that will be available to all files in module
- can be present in each test sub-folder
- if multiple files are present in a hierarchy, all of them are executed
