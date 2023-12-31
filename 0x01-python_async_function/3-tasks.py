#!/usr/bin/env python3
"""function task_wait_random that takes an integer
max_Delay adn returns a asyncio.task"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """returns asyncio.Task object"""
    return asyncio.create_task(wait_random(max_delay))
