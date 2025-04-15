def get_min_max(datas):
    try:
        datas = iter(datas)
        mini = maxi = next(datas)
        for i in datas:
            if mini > i:
                mini = i
            elif maxi < i:
                maxi = i
    except StopIteration:
        return None
    return mini, maxi


iterable = [6, 4, 2, 33, 19, 1]

print(get_min_max(iterable))

iterable = iter([])
print(get_min_max(iterable))

data = iter(range(100_000_000))

print(get_min_max(data))