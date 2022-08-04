#!/usr/bin/env python3
"""func complex input and output
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """func to return to_kv of function
    """
    return (k, v ** 2)
