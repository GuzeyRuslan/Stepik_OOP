def numbers_sum(elems):
    """Принимает список и возвращает сумму его чисел(int, float),
    игнорируя нечисловые объекты. 0 - если в списке чисел нет."""
    total = 0
    nums_list = [val for val in elems if isinstance(val, float) or isinstance(val, int)]
    if len(nums_list) != 0:
        total = sum(val for val in elems if isinstance(val, float) or isinstance(val, int))
    return total

print(numbers_sum([1, '2', 3, 4, 'five']))
print(numbers_sum.__doc__)