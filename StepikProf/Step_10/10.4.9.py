class Square:
    def __init__(self, n):
        self.n = n
        self.limit = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.limit > self.n:
            raise StopIteration
        else:
            self.limit += 1
            return (self.limit - 1) ** 2

squares = Square(10)

print(list(squares))

squares = Square(2)

print(next(squares))
print(next(squares))