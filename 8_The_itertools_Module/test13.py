from itertools import dropwhile
from itertools import filterfalse


def greater_than_five(x):
    return x < 5


print(list(dropwhile(greater_than_five, [6, 6, 7, 8, 9, 3, 2, 1])))
print(list(filterfalse(greater_than_five, [6, 6, 7, 8, 9, 3, 2, 1])))