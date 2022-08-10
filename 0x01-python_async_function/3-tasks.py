#!/usr/bin/env python3
"""function to return an async task
"""
import asyncio
from typing import Coroutine
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """fuuction to return an
    asyncronous task
    """
    return asyncio.Task(wait_random(max_delay))
