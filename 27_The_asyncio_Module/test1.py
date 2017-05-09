# python 3.4

import asyncio


@asyncio.coroutine
def my_coro():
    yield from func()