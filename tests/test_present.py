import pytest 
from lib.present import *

# Wrap - raises error if contents is not none
# Unwrap - raises error if contents is None
# Unwrap - returns contents if it isn't None.

def test_wrap_raises_error_if_contents_not_none():
    present = Present()
    present.wrap("football")
    with pytest.raises(Exception) as err:
        present.wrap("toy")
    error_message = str(err.value)
    assert error_message == "A contents has already been wrapped."


def test_unwrap_raises_error_if_contents_none():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped."

def test_unwrap_returns_contents_if_contents_not_none():
    present = Present()
    present.wrap("football")
    assert present.unwrap() == "football"

def test_wrap_already_wrapped_preserves_first_wrapped():
    present = Present()
    present.wrap("football")
    with pytest.raises(Exception) as e:
        present.wrap("toy")
    assert present.unwrap() == "football"