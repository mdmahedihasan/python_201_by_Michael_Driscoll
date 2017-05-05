from itertools import dropwhile


print(list(dropwhile(lambda x: x > 5, [6, 4, 6, 4, 1])))