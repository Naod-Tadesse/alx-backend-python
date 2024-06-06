#!/usr/bin/env python3
"""annotate the paramaters of the functions"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """elements with type annotations"""
    return [(i, len(i)) for i in lst]
