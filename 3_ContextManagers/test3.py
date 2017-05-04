from contextlib import contextmanager


@contextmanager
def closing(db):
    try:
        yield db.conn()
    finally:
        db.close()