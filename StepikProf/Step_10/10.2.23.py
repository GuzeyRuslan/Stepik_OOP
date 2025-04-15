def starmap(func, datas):
    out_list = []
    for data in datas:
        out_list.append(func(*data))
    return iter(out_list)

pairs = [(1, 3), (2, 5), (6, 4)]

print(*starmap(lambda a, b: a + b, pairs))