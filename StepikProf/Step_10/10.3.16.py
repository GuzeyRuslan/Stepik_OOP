from random import randint

def random_numbers(left, right):
    try:
        return iter(lambda: randint(left, right), left - 1)
    except TypeError:
        return None

iterator = random_numbers(1, 1)

print(next(iterator))
print(next(iterator))

iterator = random_numbers(1, 10)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))