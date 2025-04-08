def my_print(func):
    def wrapper(*args, **kwargs):
        args = tuple(map(lambda i: i.upper(), args))
        return func(*args, **kwargs)
    return wrapper


my_print = my_print(print('hi', 'there', end='!'))
