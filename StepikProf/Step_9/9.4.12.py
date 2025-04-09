old_print = print

def print(*args, sep=' ', end='\n'):
    out_list = []
    for word in args:
        if isinstance(word, str):
            out_list.append(word.upper())
        else:
            out_list.append(word)
    old_print(*out_list, sep=sep.upper(), end=end.upper())

print('bee', 'geek', sep=' and ', end=' wow')
print('beegeek', [1, 2, 3], 4) 