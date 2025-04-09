def my_pow(number):
    my_list = []
    if number == 0:
        my_list.append(number)
    while number > 0:
        my_list.append(number % 10)
        number //= 10
    my_list = my_list[::-1]

    result = sum(map(lambda x: x[1] ** x[0], enumerate(my_list, 1)))
    return result

print(my_pow(139))

