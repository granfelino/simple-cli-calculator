"""Group of tests testing the the calc.operations module"""

import pytest
from calc import operations as ops

def test_add():
    assert ops.add([1, 2, 3]) == 6
    assert ops.add([10, 20, 1]) == 31

def test_subtract():
    assert ops.subtract([1, 2, 3]) == -4
    assert ops.subtract([10, 2]) == 8

def test_multiply():
    assert ops.multiply([3, 4, 2]) == 24
    assert ops.multiply([1, 2, 3]) == 6

def test_divide():
    assert ops.divide([2, 2]) == 1
    assert ops.divide([50, 2, 5]) == 5

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        ops.divide([10, 0])
