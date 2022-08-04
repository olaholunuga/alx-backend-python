#!/usr/bin/env python3
"""duck
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """method to return first safe element of sequence
    """
    if lst:
        return lst[0]
    else:
        return None
