#!/usr/bin/env python3
"""
Concurrent coroutines
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """
    An asynchronous generator that yields a random number
    between 0 and 10 every 1 second,
    for a total of 10 times.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
