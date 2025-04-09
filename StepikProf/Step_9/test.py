def outer(x, y=2):
    def inner(z=y):
        return x, z
    x, y = None, None
    return inner

print(outer(10)())