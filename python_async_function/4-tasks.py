#!/usr/bin/env python3
"""
4. Tasks
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """execute multiple coroutines at the same time"""
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
