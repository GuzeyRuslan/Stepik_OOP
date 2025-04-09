def polynom(x):
    res = x ** 2 + 1
    if not hasattr(polynom, 'values'):
        polynom.values = {res}
    else:
        polynom.values.add(res)
    return res


print(polynom(5))
print(polynom(3))
print(polynom.values)