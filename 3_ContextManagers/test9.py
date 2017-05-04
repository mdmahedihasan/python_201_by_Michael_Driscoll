from contextlib import contextmanager


@contextmanager
def single():
    print("yielding")
    yield
    print("exiting context manager")

context = single()
with context:
    pass
with context:
    pass