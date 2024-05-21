"""
This module takes in arguments via Fire and prints them.
"""

from fire import Fire


def print_arguments(*args, **kwargs):
    """
    This function takes in a set of arguments and keyword arguments, and prints them in order, first
    values in args and each of their type, then each of the key and values in kwargs, and their
    respective type.

    Parameters
    ----------
    args : Any
        A set of arguments.
    kwargs : Any
        A set of keyword arguments.
    """

    # Print args and their types.
    #
    if args:
        print("=== Printing arguments ===")
    for i, val in enumerate(args):
        print(f"Argument {i}: {repr(val)}")
        print(f"Type: {type(val)}")

    # Print kwargs and their types.
    #
    if kwargs:
        print("=== Printing keyword arguments ===")
    for key, val in kwargs.items():
        print(f"{key}: {repr(val)}")
        print(f"Type: {type(val)}")


def main():
    Fire(print_arguments)


if "__main__" == __name__:
    main()
