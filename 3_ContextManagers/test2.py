from contextlib import contextmanager


@contextmanager
def file_open(path):
    try:
        f_obj = open(path, "w")
        yield f_obj
    except OSError:
        print("we had an error!")
    finally:
        print("closing file")
        f_obj.close()


if __name__ == '__main__':
    with file_open('test.txt') as fobj:
        fobj.write("testing context manager")