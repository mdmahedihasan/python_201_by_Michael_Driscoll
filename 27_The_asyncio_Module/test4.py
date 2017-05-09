import asyncio
import functools


def event_handler(loop, stop=False):
    print("event handler called")
    if stop:
        print("stopping the loop")
        loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        # loop.call_soon(functools.partial(event_handler, loop))
        # loop.call_later(1, event_handler, loop)
        current_time = loop.time()
        loop.call_at(current_time + 300, event_handler, loop)
        print("starting event loop")
        loop.call_soon(functools.partial(event_handler, loop, stop=True))
        loop.run_forever()
    finally:
        print("closing event loop")
        loop.close()