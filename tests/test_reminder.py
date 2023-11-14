import pytest # type: ignore
from lib.reminder import *

def test_reminder_raises_an_error_when_no_task_is_set():
    reminder = Reminder("Amy")
    with pytest.raises(Exception) as err:
        reminder.remind()
    error_message = str(err.value)
    assert error_message == "No reminder set!"