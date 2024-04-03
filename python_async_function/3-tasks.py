import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task that waits for a random amount of time
    up to max_delay seconds.
    """
    # Schedule the execution of wait_random using asyncio.create_task
    task = asyncio.create_task(wait_random(max_delay))
    return task
