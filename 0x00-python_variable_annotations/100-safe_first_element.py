#!/usr/bin/env python3
"""duck
"""
from typing import Any, Sequence, Union

NoneType = None

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
