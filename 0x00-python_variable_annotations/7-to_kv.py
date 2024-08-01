#!/usr/bin/env python3
"""Module for creating a tuple from a string and int/float."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and the square of an int/float.

    Args:
        k (str): The string input.
        v (Union[int, float]): The int or float input.

    Returns:
        Tuple[str, float]: A tuple containing the string and the square of v.
    """
    return (k, float(v ** 2))
