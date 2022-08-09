#!/usr/bin/env python3
"""writing asyncronous function
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """function to take an int of float and return
    a random number between 0 and max_delay after
    """
    n = random.random() * max_delay
    await asyncio.sleep(n)
    return n
