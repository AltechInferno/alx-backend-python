#!/usr/bin/env python3
"""
function for returning the first element
    of a list, or None if the list is empty.
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    returns the first element of a sequence, or None if
        sequence is empty.

    Parameters:
    lst (Sequence): sequence to process.

    Returns:
    Union[object, None]: first element of the sequence, or None if the
        sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
