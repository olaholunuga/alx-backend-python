#!/usr/bin/env python3
"""spawn function a number of times
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """function to spawn wait_random a
    number of times
    """
    result_list = []
    for _ in range(n):
        m = await wait_random(max_delay)
        result_list.append(m)
    return result_list

