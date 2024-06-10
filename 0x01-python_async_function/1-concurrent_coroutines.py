#!/usr/bin/env python3
"""
spawn random n times with specified delay
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """delay n times to output n random numbers"""
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays

if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 10)))
