'Test for capitalize_case.py'
import pytest

from capital_case import *

def test_capital_case():
    'Main purpose of function'
    assert capital_case('semaphore') == 'Semaphore'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)
