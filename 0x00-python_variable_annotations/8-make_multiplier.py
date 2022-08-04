#!/usr/bin/env python3
"""function to return a fuction
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function to return callable function
    that can be called
    """
    anon_func: Callable[[float], float] = lambda x: float(x) * multiplier
    return anon_func
