#!/usr/bin/env python3
"""spawn function a number of times
"""
import asyncio
from typing import List, Union
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[Union[int, float]]:
    """modified function to spawn wait_random a
    number of times
    """
    result_list = await asyncio.gather(
            *(task_wait_random(max_delay) for i in range(n))
            )
    return sorted(result_list)
