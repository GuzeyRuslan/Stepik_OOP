def get_id(names: list, name):
    if isinstance(name, str):
        if name.istitle() and name[1:].isalpha() and name[1:].islower():
            names.append(name)
            return len(names)
        else:
            raise ValueError('Имя не является корректным')
    else:
        raise TypeError('Имя не является строкой')

names = ['Timur', 'Anri', 'Dima', 'Roma', 'Gvido', 'Rosy', 'Soslan', 'Natasha', 'Arthur']
name = 'Arthur'

print(get_id(names, name))

