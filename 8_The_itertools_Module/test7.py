import operator
from itertools import accumulate


print(list(accumulate(range(1, 7), operator.mul)))