#!/usr/bin/env python3
"""wait_n: takes 2 int args that spawn wait_random
n times with specified max_delay.
SHould return the list of all the delays in ascending order
"""

import asyncio
from typing import List
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    spawns wait_random n times and return a list of all delays
    concurrently
    """

    tasks = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    delays = []

    while tasks:
        done, tasks = await asyncio.wait(tasks,
                                         return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            delay = task.result()
            delays.append(delay)
    return delays
