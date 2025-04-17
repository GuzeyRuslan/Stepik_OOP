def is_iterator(obj):
    try:
        return obj == iter(obj)
    except TypeError:
        return None

print(is_iterator([1, 2, 3, 4, 5]))

beegeek = filter(None, [0, 0, 1, 1, 0, 1])

print(is_iterator(beegeek))