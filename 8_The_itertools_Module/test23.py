from itertools import product

arrays = [(-1, 1), (-3, 3), (-5, 5)]
print(list(product(*arrays)))
print(list(product(arrays)))
print(*arrays)
print(arrays)