#!/usr/bin/env python3
"""0. Async Generator
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """a coroutine called async_generator"""
    for i in range(10):
        ran_num = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield ran_num
