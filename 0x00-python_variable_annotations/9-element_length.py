#!/usr/bin/python3
"""Annotate element_length function
Has lst as arg and return the values of the list"""


from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return a tuple of the elem in the list"""
    return [(i, len(i)) for i in lst]
