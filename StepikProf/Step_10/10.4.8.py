class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times
        self.limit = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.limit > self.times:
            raise StopIteration
        else:
            self.limit += 1
            return self.obj

bee = BoundedRepeater('bee', 3)

print(next(bee))
print(next(bee))
print(next(bee))
print(next(bee))
print(next(bee))
