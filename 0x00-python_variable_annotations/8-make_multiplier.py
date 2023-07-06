#!/usr/bin/env python3
"""Function make_multiplier: take float multiplier
and return a function that multiplies a float by
multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float with
    a multiplier"""
    def mul(n: float) -> float:
        return multiplier * n
    return mul
