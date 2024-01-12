#!/usr/bin/env python3
"""
a function for safely getting a value from
    a mapping.
"""
from typing import Any, Mapping, Union, TypeVar

TV = TypeVar('T')
Res = Union[Any, TV]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    gets the value for a given key in a mapping, or returns
        a default value if key is not in the mapping.

    Parameters:
    dct (Mapping): mapping to get the value from.
    key (Any): key to look up in the mapping.
    default (Union[TV, None]): default value to return if key is not
        in the mapping.

    Returns:
    Union[Any, TV]: value for the key in the mapping
    """
    if key in dct:
        return dct[key]
    else:
        return default
