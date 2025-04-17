path = input()
try:
    with open(path, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Файл не найден")