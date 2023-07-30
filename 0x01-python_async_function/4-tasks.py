#!/usr/bin/env python3
"""
task_wait_n: an async routine called task_wait_n that takes in
            2 int arguments (in this order): n and max_delay.
            It will spawn task_wait_random n times with the
            specified max_delay.
"""


import asyncio
from typing import List
import random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    spawns task_wait_random n times and return a list of all delays
    concurrently
    """

    tasks = []
    tasks = [task_wait_random(max_delay) for i in range(n)]

    delays = []

    while len(tasks):
        done, tasks = await asyncio.wait(tasks,
                                         return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            delay = task.result()
            delays.append(delay)
    return delays
