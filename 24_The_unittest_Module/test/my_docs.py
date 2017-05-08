def add(a, b):
    """
    Return the addition of the arguments: a + b
    
    >>> add(1, 2)
    3
    >>> add(-1, 10)
    9
    >>> add('a', 'b')
    'ab'
    >>> add(1, '2')
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a + b


def subtract(a, b):
    """
    Returns the result of subtracting b from a
    
    >>> subtract(2, 1)
    1
    >>> subtract(10, 10)
    0
    >>> subtract(7, 10)
    -3
    """
    return a - b