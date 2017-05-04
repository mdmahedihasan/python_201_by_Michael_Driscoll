from functools import singledispatch


@singledispatch
def add(a, b):
    raise NotImplementedError("unsupported type")


@add.register(int)
def _(a, b):
    print("first argument is of type ", type(a))
    print(a + b)


@add.register(str)
def _(a, b):
    print("first argument is of type ", type(a))
    print(a + b)


@add.register(list)
def _(a, b):
    print("first argument is of type ", type(a))
    print(a + b)


if __name__ == '__main__':
    add(1, 2)
    add("python", " programming")
    add([1, 2, 3], [4, 5, 6])