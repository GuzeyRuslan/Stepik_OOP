import functools

def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            temp = ""
            for i in range(times):
                temp = func(*args, **kwargs)
            return temp
        return wrapper
    return decorator


@repeat(3)
def say_beegeek():
    '''documentation'''
    print('beegeek')


say_beegeek()