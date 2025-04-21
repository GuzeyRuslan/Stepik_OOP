def get_weekday(number):
    if isinstance(number, int):
        if 1 <= number <= 7:
            weekday = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье"}
            return weekday[number]
        else:
            raise ValueError('Аргумент не принадлежит требуемому диапазону')
    else:
        raise TypeError('Аргумент не является целым числом')



try:
    print(get_weekday('hello'))
except Exception as err:
    print(err)
    print(type(err))
