#!/usr/bin/env python3
"""Module for safely getting the first element of a sequence."""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely return the first element of a sequence.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, None]: the sequence or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
