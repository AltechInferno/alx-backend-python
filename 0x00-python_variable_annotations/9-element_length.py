#!/usr/bin/env python3
"""
finding the length of each element in a list of strings.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    takes a list of strings and returns a list of tuples,
        where each tuple contains a string and the length of that string.

    Parameters:
    lst (List[str]): list of strings to process.

    Returns:
    List[Tuple[str, int]]: list of tuples, where each contains
        a string and length of that string.
    """
    return [(i, len(i)) for i in lst]
