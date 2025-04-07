class User():
    def __init__(self, name = "", age = 0):
        if type(name) == str and name.isalpha():
            self._name = name
        else:
            raise ValueError("Некорректное имя")
        if type(age) == int and 0 <= age <= 110:
            self._age = age
        else:
            raise ValueError("Некорректный возраст")

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if type(new_name) == str and new_name.isalpha():
            self._name = new_name
        else:
            raise ValueError("Некорректное имя")

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if type(new_age) == int and 0 <= new_age <= 110:
            self._age = new_age
        else:
            raise ValueError("Некорректный возраст")

