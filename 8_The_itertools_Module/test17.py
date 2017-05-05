from itertools import starmap


def add(a, b):
    return a + b


for item in starmap(add, [(2, 5), (4, 5)]):
    print(item)