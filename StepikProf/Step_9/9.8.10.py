import functools

def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if isinstance(func(*args, **kwargs), str):
            return func(*args, **kwargs)
        else:
            raise TypeError
    return wrapper




@returns_string
def add(a, b):
    return a + b

try:
    print(add(3, 7))
except TypeError as e:
    print(type(e))


@returns_string
def beegeek():
    return 'beegeek'

print(beegeek())