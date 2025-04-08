def do_twice(func):
    def wrapper(*args, **kwargs):
        f1 = func(*args, **kwargs)
        f2 = func(*args, **kwargs)
        return f2
    return wrapper
