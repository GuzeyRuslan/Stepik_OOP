def filterfalse(func, iterable):
    out_list = []
    if func is None:
        for i in iterable:
            if not i:
                out_list.append(i)
    else:
        for i in iterable:
            if not func(i):
                out_list.append(i)
    return iter(out_list)


objects = [0, 1, True, False, 17, []]

print(*filterfalse(None, objects))

numbers = (1, 2, 3, 4, 5)

print(*filterfalse(lambda x: x % 2 == 0, numbers))