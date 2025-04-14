import functools

def prefix(string, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if to_the_end:
                return func(*args, **kwargs) + string
            return string + func(*args, **kwargs)
        return wrapper
    return decorator


# @prefix('€')
# def get_bonus():
#     return '2000'
#
#
# print(get_bonus())
#
#
# @prefix('$$$', to_the_end=True)
# def get_bonus():
#     return '2000'
#
#
# print(get_bonus())
#
# @prefix(' online-school', to_the_end=True)
# def beegeek():
#     '''beegeek docs'''
#     return 'beegeek'
#
# print(beegeek.__name__)
# print(beegeek.__doc__)
# print(beegeek())


@prefix('online-school ')
def make_lower(string, lower=True):
    '''makes string upper or lower'''
    if lower:
        return string.lower()
    return string.upper()


print(make_lower.__name__)
print(make_lower.__doc__)
print(make_lower('beegeek', False))