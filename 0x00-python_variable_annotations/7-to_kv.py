#!/usr/bin/env python3
"""
Function to_kv: takes str k and an int or float v
return tuple
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return tuple where first elem is k and second is
    square of int/float of v"""
    return (k, v * v)
