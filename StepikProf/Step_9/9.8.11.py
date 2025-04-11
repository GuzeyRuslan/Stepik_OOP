import functools

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}")
        temp = func(*args, **kwargs)
        if isinstance(temp, str):
            print(f"TRACE: возвращаемое значение {func.__name__}(): '{func(*args, **kwargs)}'")
        else:
            print(f"TRACE: возвращаемое значение {func.__name__}(): {func(*args, **kwargs)}")
        return func(*args, **kwargs)
    return wrapper


@trace
def func(nums):
    '''прекрасная функция'''
    return list(i ** 2 for i in nums)


print(func.__name__)
print(func.__doc__)
func([1, 2, 3, 4, 5, 6])


print()
@trace
def beegeek():
    '''beegeek docs'''
    return 'beegeek'

print(beegeek())
print(beegeek.__name__)
print(beegeek.__doc__)