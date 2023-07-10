#!/usr/bin/env python3
"""measure_time(n, max_delay):
measures total execution time for wait_n(n, max_delay)
Returns total_time / n"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """returns total time for each concurrent"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
