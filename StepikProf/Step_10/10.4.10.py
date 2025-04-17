class Fibonacci:
    def __init__(self):
        self.cur = 1
        self.prev = 0
        self.next = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.next = self.cur + self.prev
        self.prev, self.cur = self.cur, self.next
        return self.prev

fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
