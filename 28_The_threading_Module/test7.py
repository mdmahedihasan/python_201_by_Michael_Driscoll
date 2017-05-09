import threading


total = 0
lock = threading.Lock()


def do_something():
    lock.acquire()
    
    try:
        print("lock acquired in the do_something function")
    finally:
        lock.release()
        print("lock released in the do_something function")
    return "done do_something"


def do_something_else():
    lock.acquire()

    try:
        print("lock acquired in the do_something_else function")
    finally:
        lock.release()
        print("lock released in the do_something_else function")
    return "done do_something_else"


if __name__ == '__main__':
    result_one = do_something()
    result_two = do_something_else()