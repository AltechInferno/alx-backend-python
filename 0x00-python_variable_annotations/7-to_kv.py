#!/usr/bin/env python3
"""
function for creating a tuple with a string
    and the square of an int or float as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    takes a string and an int or float, and returns a tuple with
        the string and the square of the int or float as a float.

    Parameters:
    k (str): string to include in the tuple.
    v (Union[int, float]): int or float to square.

    Returns:
    Tuple[str, float]: tuple with the string k and the square of v as a
        float.
    """
    return (k, float(v ** 2))
