def remove_marks(text, marks):
    remove_marks.__dict__.setdefault('count', 0)
    count_sym = 0
    for sym in marks:
        count_sym += text.count(sym)
    i = 0
    temp = len(text)
    while len(text) > temp - count_sym:
        if text[i] in marks:
            text = text[:i] + text[i + 1:] # Ты забыл про replace((
            continue
        i += 1
    remove_marks.count += 1
    return text


marks = '.,!?'
text = 'Are you listening? Meet my family! There are my parents, my brother and me.'

for mark in marks:
    print(remove_marks(text, mark))

print(remove_marks.count)

