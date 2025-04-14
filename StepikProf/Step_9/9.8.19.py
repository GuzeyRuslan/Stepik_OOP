import functools


def strip_range(start, end, char='.'):  # DO [start:end)
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)[:start] + char * (end - start) + func(*args, **kwargs)[end:] if end <= len(
                func(*args, **kwargs)) else func(*args, **kwargs)[:start] + char * (len(func(*args, **kwargs)) - start)

        return wrapper

    return decorator


@strip_range(3, 5)
def beegeek():
    return 'beegeek'


print(beegeek())
