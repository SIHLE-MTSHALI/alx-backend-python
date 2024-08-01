#!/usr/bin/env python3
"""Module for calculating the length of list elements."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the input list.

    Args:
        lst (Iterable[Sequence]): The input iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples,
    """
    return [(i, len(i)) for i in lst]
