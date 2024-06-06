#!/usr/bin/env python3
"""multiplier """

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """multiplier maker"""
    def multiplier_function(val: float) -> float:
        return val * multiplier
    return multiplier_function
