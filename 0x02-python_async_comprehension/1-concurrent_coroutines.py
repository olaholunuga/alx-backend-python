#!/usr/bin/env python3
"""spawn function a number of times
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """function to spawn wait_random a
    number of times
    """
    result_list = await asyncio.gather(
            *(wait_random(max_delay) for i in range(n))
            )
    return sorted(result_list)
