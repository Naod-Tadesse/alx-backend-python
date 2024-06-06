#!/usr/bin/env python3
"""duck typed annotations"""

from typing import Sequence, Any, Union


def safe_first_element(lt: Sequence[Any]) -> Union[Any, None]:
    """duck typed annotations"""
    if lt:
        return lt[0]
    else:
        return None
