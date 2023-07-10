#!/usr/bin/env python3
"""
Wait_Random: that awaits for random delay between
0 - max_delay
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """takes a delay integer and awaits a random delay
    and returns the delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
