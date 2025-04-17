class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.key = iter(data)

    def __iter__(self):
        return self

    def __next__(self):
        key = next(self.key)
        value = self.data[key]
        return key, value

pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})

print(*pairs)
