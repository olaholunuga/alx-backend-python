#!/usr/bin/env python3
"""function to measure time lapse of coroutine
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """to measure time lapse of corutine
    """
    s = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - s
    return total_time / n
