import pytest #type: ignore

from lib.password_checker import *

# Check that password equal to 8 returns True
# Check that password greater than 8 returns True; test a couple of lengths
# Check that if password is 7 or less it returns error message:
# Need to test for 7, 6, 5, 4, 3, 2, 1, 0

def test_password_length_equal_8():
    password_checker = PasswordChecker()
    assert password_checker.check("password") == True

def test_password_length_greater_than_8():
    password_checker = PasswordChecker()
    assert password_checker.check("password1") == True
    assert password_checker.check("password12") == True
    assert password_checker.check("password123") == True
    assert password_checker.check("password1234") == True

def test_password_length_equal_7_returns_error():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("tester1")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

def test_password_length_6_returns_error_message():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("test12")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

def test_password_length_5_returns_error_message():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("test1")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

def test_password_length_4_returns_error_message():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("test")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

def test_password_length_3_returns_error_message():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("123")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

def test_password_length_2_returns_error_message():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("12")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

def test_password_length_1_returns_error_message():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("1")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

def test_password_length_0_returns_error_message():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."