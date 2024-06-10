#!/usr/bin/env python3
"""
similar to task 3
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """at n random times"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
