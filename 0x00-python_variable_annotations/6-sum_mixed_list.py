#!/usr/bin/env python3
"""
a function for summing list values.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    computes the sum of a list of integers and floats,
        returns the result as a float.

    Parameters:
    mxd_lst (List[Union[int, float]]): list of integers and floats to sum.

    Returns:
    float: sum of the elements in mxd_lst.
    """
    return sum(mxd_lst)
