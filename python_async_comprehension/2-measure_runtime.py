#!/usr/bin/env python3
"""
2. Run time for four parallel comprehensions
"""

import asyncio
from time import time
async_generator = __import__('0-async_generator').async_generator
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.
    """
    s_t = time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    e_t = time()
    return e_t - s_t
