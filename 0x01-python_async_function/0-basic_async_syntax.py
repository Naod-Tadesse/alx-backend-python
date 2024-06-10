#!/usr/bin/env python3
"""
basic async code
"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """basic delay function"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
