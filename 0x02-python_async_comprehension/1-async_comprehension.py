#!/usr/bin/env python3
"""
Async_comprehension:
Collects 10 random numbers using async comprehension
over async_generator
Returns 10 random numbers
"""


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """returns 10 random numbers"""
    return [val async for val in async_generator()]
