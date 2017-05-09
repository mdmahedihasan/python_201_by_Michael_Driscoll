from concurrent.futures import ThreadPoolExecutor


def wait_forever():
    my_future = executor.submit(zip, [1, 2, 3], [4, 5, 6])
    return my_future


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=3)
    fut = executor.submit(wait_forever)
    print(fut)

    result = fut.result()
    print(list(result.result()))
