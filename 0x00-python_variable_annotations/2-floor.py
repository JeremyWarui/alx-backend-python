#!/usr/bin/python3
"""
Function floor that takes float and returns floor of float
"""


def floor(n: float) -> int:
    """return largest int value less than or equal to n"""
    return int(n) if n >= 0 else int(n) - 1
