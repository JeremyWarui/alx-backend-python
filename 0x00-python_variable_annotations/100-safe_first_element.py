#!/usr/bin/env python3
"""Augment with correct duck-typed annotations
Function safe_first_element: returns first elem
or none
"""


from types import NoneType
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """returns first elem or none"""
    if lst:
        return lst[0]
    else:
        return None
