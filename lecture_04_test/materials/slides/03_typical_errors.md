## Typical errors
- Many test in a single test
- Test coupling
- Test wrong exception
- Assert nothing
- Not detailed assert
- Assert floating-point numbers
- Test your mock
- Test unreliable sources (fail with no reason)
- Cleanup in test body
- Expected value is calculated
- Test generation inside test

## Many test in a single test

- Error can be hidden by other errors
- More chance to make an error in tests

```python
def test_user_...():
    admin = User(...)
    assert admin.get....
    
    user = User(...)
    assert user.get....
    
    guest = User(...)
    assert guest.get....
```

## Test coupling

If you run a single test it will fail
If you run test in different order some will fail
If you try to parallelize test running they will fail from time to time

```python
state = True


def test_state_set_state():
    global state
    state = False
    assert state is False


def test_get_state():
    assert state is False
```

## Test wrong exception

You can have couple of cases:
- Test passed, but a function is not working as expected.
- Test is wrong and function is not tested.

```python
def is_positive(text: int):
    if text == 0:
        raise ValueError("undefined is not a number")
```

### bad
```python
def test_negative_integer_raises_and_error():
    with pytest.raises(ValueError):
        is_positive("-1")
```

### good
```python
def test_negative_integer_raises_and_error():
    with pytest.raises(ValueError, match="Positive number required"):
        is_positive("-1")
```

## Assert nothing
This check that code does not produce an exception

```python
def test_fibonacci():
    check_fibonacci([3, 1])
```

## Not detailed assert
Check that result is produced but does not change which one  

```python
def test_minor_and_major():
    assert major_and_minor_elem([1, 2, 3])
```

## Assert floating-point 

Implementation of floating-point is well-know source of trouble.
You change a test a little, and boom it fails.

### bad
```python
def test_float_bad():
    assert 0.1 + 0.2 == 0.3
```
   
```
    def test_float_bad():
>       assert 0.1 + 0.2 == 0.3
E       assert 0.30000000000000004 == 0.3
E         +0.30000000000000004
E         -0.3
```

### good
 
```python
def test_float_good():
    assert 0.1 + 0.2 == pytest.approx(0.3)
```

## Test your mock
```python
def connection_mock(url):
    return {"message": "OK"}


def test_connection():
    assert connection_mock("http://localhost") == {"message": "OK"}
```

## Test unreliable sources

If test is passed or failed depends not on you, but on some 3d party.

```python
def test_connection():
    assert connect("http://production.com/api/v3/status") == {"message": "OK"}
```

## Cleanup in test body

If test fails, cleanup is not happen

```python
def test_file():    
    create_txt_file(text, "test_text.txt")
    assert count_punctuation_chars("test_text.txt") == 6
    os.remove("test_text.txt")
```

## Expected value is calculated

## bad
```python

def is_posistive(n):
    return True if n else False

def test_is_positive__reuse_code():
    expected = is_posistive(-1)
    assert is_posistive(-1) == expected
   
    
def test_is_positive__copy_code():
    def _get_expected_value(num):
        return True if num else False
    
    expected = _get_expected_value(-1)
    assert is_posistive(-1) == expected
```

## good
```python
def test_negative_value_is_false():
    assert is_posistive(-1) is False
```

## Test generation inside test
Error prone, complex. 

### bad
```python
def test_is_positive():
    for x in range(-10, 10):
        if x <= 0:
            assert is_positive(x) is False
        else:
            assert is_positive(x) is True
```

Split to separate tests, use test generation `pytest.mark.parametrize`. 

### bad
```python
def test_is_positive():
    res = is_positive(-1)
    if not res:
        assert False
```

### good
```python
def test_is_positive():
    assert is_positive(-1) is False
```
