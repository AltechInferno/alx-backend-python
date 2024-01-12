#!/usr/bin/env python3
"""
provides a function for creating a function that
    multiplies a float by a multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float as an argument and returns a function that
        multiplies a float by the multiplier.

    Parameters:
    multiplier (float): multiplier to use in the returned function.

    Returns:
    Callable[[float], float]: A function that multiplies a float by the
        multiplier.
    """
    def multiply(n: float) -> float:
        """
        multiplies a float by the multiplier.

        Parameters:
        n (float): float to multiply by the multiplier.

        Returns:
        float: result of multiplying n by the multiplier.
        """
        return n * multiplier
    return multiply
