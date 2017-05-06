import random
import time


def timerfunc(func):
    def function_timer(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "the runtime for {func} took {time} seconds to complete"
        print(msg.format(func=func.__name__, time=runtime))
        return value
    return function_timer


@timerfunc
def long_runner():
    for x in range(5):
        sleep_time = random.choice(range(1, 5))
        time.sleep(sleep_time)


if __name__ == '__main__':
    long_runner()