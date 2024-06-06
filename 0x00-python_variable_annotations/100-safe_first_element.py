#!/usr/bin/env python3
"""duck typed annotations"""

import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """duck typed annotations"""
    if lst:
        return lst[0]
    else:
        return None
