from functools import singledispatch


@singledispatch
def add(a: int, b: int) -> int:
    raise NotImplementedError("unsupported type")


@add.register(int)
def _(a, b):
    print("first argument is of type ", type(a))
    print(a + b)
    return a + b


@add.register(str)
def _(a: str, b: str) -> str:
    print("first argument is of type ", type(a))
    print(a + b)
    return a + b


@add.register(list)
def _(a: list, b: list) -> list:
    print("first argument is of type ", type(a))
    print(a + b)
    return a + b