#!/usr/bin/env python3
"""TypeVar
"""
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')
ReType = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> ReType:
    """function to savfaly get value
    """
    if key in dct:
        return dct[key]
    else:
        return default
