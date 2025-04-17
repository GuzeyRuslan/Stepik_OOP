class PowerOf:
    def __init__(self, number):
        self.num = number
        self.degree = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.degree += 1
        return self.num ** self.degree

power_of_two = PowerOf(2)

print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))