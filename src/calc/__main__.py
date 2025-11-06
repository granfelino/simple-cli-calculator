"""
__main__.py

CLI interface for the calculator package.

This module serves as the entry point when running the package
by `python -m calc`. It parses user input, dispatches operations
to the functions in `operations.py` and displays the result.

Usage
-----
python -m calc add 1 2
python -m calc subtract 1 2
python -m calc multiply 1 2
python -m calc divide 1 2
"""

import argparse
import sys
import logging
import calc.operations as ops

OP_ADD = "add"
OP_SUB = "subtract"
OP_MUL = "multiply"
OP_DIV = "divide"

logging.basicConfig(
        filename="calc.log",
        filemode="w",
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def get_parser() -> argparse.ArgumentParser:
    """Creates, prepares and returns an ArgumentParser instance.

    ArgumentParser object is filled with most important information. Two
    positional arguments are added to it: 
        - type of operation
        - numbers to operate on
    
    This function does not take any parameters.

    Returns
    -------
    argsparse.ArgumentParser
        An instance of ArgumentParser object.
    """

    parser = argparse.ArgumentParser(prog="CLICalc",
                                     description="CLI calculator app.")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"])
    parser.add_argument("numbers", nargs="*", type=float)
    return parser

def get_valid_args() -> list[str]:
    """Returns the list of CLI argument without the program name.

    This function does not take any parameters.

    Returns
    -------
    list[str]
        List of CLI arguments.
    """

    return sys.argv[1:]

def print_result(op: str, nums: list[float], ret: float) -> None:
    """Prints a readable output of the calculator program.

    Parameters
    ----------
    op : str
        The operation that was performed.
    nums : list[float]
        The list of float values that the operation was performed on.
    ret : float
        The result of the operation on the list of float values.
    """

    print("Operation: " + op)
    print("Numbers: " + str(nums))
    print("Result: " + str(ret))

def main() -> None:
    """Entry point of the program.

    The function requests the argument parser, parses the arguments and
    handles the calculating operation according to given arguments.

    This function does not take any arguments & returns nothing.
    """

    logger.info("Program start.")

    parser = get_parser()
    logger.info("Parser ready.")

    args = parser.parse_args(get_valid_args())
    logger.info("Arguments parsed.")

    op = args.operation
    nums = args.numbers

    operations = {
            OP_ADD : ops.add,
            OP_SUB : ops.subtract,
            OP_MUL : ops.multiply,
            OP_DIV : ops.divide,
    }

    ret = operations[op](nums)
    logger.info("Operation done.")

    print_result(op, nums, ret)



if __name__ == "__main__":
    main()
