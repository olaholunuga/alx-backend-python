#!/usr/bin/env python3
"""func to treat duck typing
"""
from typing import Sequence, Tuple, List, Iterable

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
