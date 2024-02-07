#!/usr/bin/env python3
"""1. Let's execute multiple coroutines at the same time with async
"""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """execute multiple coroutines at the same time with async"""
    delays = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return sorted(delays)
