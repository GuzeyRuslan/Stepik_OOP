import functools

def make_capitalize(func):
    @functools.wraps
    def wrapper():
        return func().capitalize()
    return wrapper

@make_capitalize
def beegeek():
    '''documentation'''
    return 'beegeek'

print(beegeek.__name__)
print(beegeek.__doc__)