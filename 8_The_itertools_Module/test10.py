from itertools import chain


numbers = list(range(5))
cmd = ['ls', '/some/dir']
print(list(chain.from_iterable([cmd, numbers])))
print(list(chain.from_iterable((cmd, numbers))))