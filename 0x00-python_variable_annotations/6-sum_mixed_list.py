#!/usr/bin/env python3
"""
Function sum_mixed_list: takes list as arg and returns their sum
as float
"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """return sun of all elements in the list"""
    sum = 0
    for num in mxd_list:
        sum += num
    return sum
