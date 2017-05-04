from functools import wraps


def another_function(func):
    @wraps(func)
    def wrapper():
        val = "the result of %s is %s" % (func(), eval(func()))
        return val
    return wrapper


@another_function
def a_function():
    return "1 + 1"


if __name__ == '__main__':
    print(a_function.__name__)