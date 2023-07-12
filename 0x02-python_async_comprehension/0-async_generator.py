#!/usr/bin/env python3
"""
A coroutine that takes no arguments
Loops 10 times each time awaiting 1 second
Then yields a random number btwn 0 - 10
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """yields a random number"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
