#!/usr/bin/env python3
"""
6. Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return sum of a mixed list"""
    return float(sum(mxd_lst))
