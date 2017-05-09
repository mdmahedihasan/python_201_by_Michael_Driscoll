from multiprocessing import Pool


def doubler(number):
    return number * 2


if __name__ == '__main__':
    numbers = [4, 10, 20]
    pool = Pool(processes=1)
    print(pool)
    print(pool.map(doubler, numbers))