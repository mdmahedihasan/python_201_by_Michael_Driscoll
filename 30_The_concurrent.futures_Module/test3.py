from concurrent.futures import ThreadPoolExecutor


def wait_forever():
    my_future = executor.submit(zip, [1, 2, 3], [4, 5, 6])
    result = my_future.result()
    print(result)


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=1)
    executor.submit(wait_forever)