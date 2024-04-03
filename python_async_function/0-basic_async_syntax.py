#!/usr/bin/env python3
"""
Basic async coroutine
"""

import asyncio
import random

async def wait_n(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a
    random amount of time between 0 and max_delay seconds.
    """
    # Generate a random delay
    delay = random.uniform(0, max_delay)
    # Wait for the generated delay
    await asyncio.sleep(delay)
    # Return the delay
    return delay
