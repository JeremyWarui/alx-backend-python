#!/usr/bin/env python3
"""
Function sum_list: takes list as arg and returns their sum
as float
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """return sun of all elements in the list"""
    sum = 0
    for num in input_list:
        sum += num
    return sum
