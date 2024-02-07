#!/usr/bin/env python3
"""8. Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a multiplier function."""

    def multiplier_function(m: float) -> float:
        """Multiply a float by the multiplier."""
        return m * multiplier

    return multiplier_function
