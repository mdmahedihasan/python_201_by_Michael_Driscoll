from multiprocessing import Pool


def doubler(number):
    return number * 2


if __name__ == '__main__':
    pool = Pool(processes=1)
    result = pool.apply_async(doubler, (25, ))
    print(result)
    print(result.get(timeout=1))