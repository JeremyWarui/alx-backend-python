#!/usr/bin/env python3
"""
measure_runtime: executes async_comprehension
four times in parallel using asyncio.gather
Should measure total runtimes and return it
"""


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """gives the time taken to run parallel coroutines"""
    start = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time.time()
    return end - start
