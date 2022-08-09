#!/usr/bin/env python3
"""python async function
"""
from typing import List, Union
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[Union[int, float]]:
    """function to return async comprehension
    """
    return [i async for i in async_generator()]
