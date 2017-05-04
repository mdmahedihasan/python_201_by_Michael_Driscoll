def another_function(func):
    def wrapper():
        """wrapping function"""
        val = "the result of %s is %s" % (func(), eval(func()))
        return val
    return wrapper


@another_function
def a_function():
    return "1 + 1"


if __name__ == '__main__':
    print(a_function.__name__)
    print(a_function.__doc__)