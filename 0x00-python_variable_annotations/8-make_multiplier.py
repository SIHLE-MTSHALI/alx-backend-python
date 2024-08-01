#!/usr/bin/env python3
"""Module for creating a function that multiplies a float by multiplier."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by multiplier.

    Args:
        multiplier (float): The multiplier.

    Returns:
        Callable[[float], float]: takes a float and returns a float.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
