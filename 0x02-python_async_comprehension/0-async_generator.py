#!/usr/bin/env python3
"""an asyncronous generator
"""
import asyncio
import random
from typing import Iterator, Union


async def async_generator() -> Iterator[Union[int, float]]:
    """asyncronous generator function
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
