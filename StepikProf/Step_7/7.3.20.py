import calendar



months = list(calendar.month_name)
try:
    number = int(input())
    if number <= 0 or number >= 12:
        raise IndexError
    print(months[number])
except IndexError:
    print("Введено число из недопустимого диапазона")
except ValueError:
    print("Введено некорректное значение")