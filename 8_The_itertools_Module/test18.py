from itertools import takewhile


print(list(takewhile(lambda x: x < 5, [1, 4, 3, 6, 4, 1])))