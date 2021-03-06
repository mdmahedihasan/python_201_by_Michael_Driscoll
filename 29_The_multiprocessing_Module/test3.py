from multiprocessing import Process, Lock


def printer(item, lock):
    lock.acquire()
    try:
        print(item)
    finally:
        lock.release()


if __name__ == '__main__':
    lock = Lock()
    items = ["a", "b", 10]
    for item in items:
        p = Process(target=printer, args=(item, lock))
        p.start()