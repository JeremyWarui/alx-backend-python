#!/usr/bin/env python3
"""Augment with correct duck-typed annotations
Function safely_get_value: returns a dict
or default value
"""


from typing import Mapping, TypeVar, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T,
                                    None] = None) -> Union[Any, T]:
    """Returns dict[key] if exists or returns default value"""
    if key in dct:
        return dct[key]
    else:
        return default
