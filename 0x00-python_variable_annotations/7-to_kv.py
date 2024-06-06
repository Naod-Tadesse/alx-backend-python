#!/usr/bin/env python3
"""this function return tuple"""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """return tuple"""
    return (k, float(v * v))
