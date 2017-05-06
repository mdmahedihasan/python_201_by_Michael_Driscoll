import time


@profile
def fast_function():
    print("i am a fast function")


@profile
def slow_func():
    time.sleep(2)
    print("i am a slow function")


if __name__ == '__main__':
    fast_function()
    slow_func()