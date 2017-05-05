from itertools import islice


iterator = islice("123456", 4)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))