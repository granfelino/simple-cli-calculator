"""
operations.py

Implements basic arithmetic functions for the CLI calculator app.

Modules
-------
logging : standard logging library
math : standard math library of Python

Functions
---------
add(nums)
subtract(nums)
multiply(nums)
divide(nums)
"""

import logging
import math

logger = logging.getLogger(__name__)

def add(nums: list[float]) -> float:
    """Adds numbers in the list.

    This function sums all the numbers given in the list and returns
    the result.

    Parameters
    ----------
    nums : list[float]
        The list of float values to be added.

    Returns
    -------
    float
        Result of addition.
    """
    
    logger.debug("Performing addition.")
    return sum(nums)

def subtract(nums: list[float]) -> float:
    """Subtracts the sum of [1:] elements from the first element of the list.

    This function subtracts the sum of [1:] elements given in the list from 
    the 0-th element and returns the reult.

    Parameters
    ----------
    nums : list[float]
        List of floats to be operated on.

    Returns
    -------
    float
        Result of subtraction.
    """

    logger.debug("Performing subtraction.")
    return nums[0] - sum(nums[1:])

def multiply(nums: list[float]) -> float:
    """Multiplies all the elements from the list.

    This function multiplies all elements of the list and retuns
    the result.

    Parameters
    ----------
    nums : list[float]
        List of floats to be operated on.

    Returns
    -------
    float
        Result of multiplication.
    """
    
    logger.debug("Performing multiplication.")
    return math.prod(nums)

def divide(nums: list[float]) -> float:
    """Divides the first element by all the other elements of the list.

    This function divides the first element by all the other elements of 
    the list and returns the result.

    Parameters
    ----------
    nums : list[float]
        List of floats to be operated on.

    Returns
    -------
    float
        Result of division.

    Raises
    ------
    ZeroDivisionError
        If any of the dividers is 0.
    """

    logger.debug("Performing division.")
    ret = nums[0]
    for i in nums[1:]:
        if i == 0:
            logger.error("Division by zero.")
            raise ZeroDivisionError("Division by zero is disallowed.")
        ret /= i
    return ret
