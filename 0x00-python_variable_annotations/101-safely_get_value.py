#!/usr/bin/env python3
"""function annotations"""

from typing import TypeVar, Dict, Any, Optional, Mapping, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """get value safely with annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
