class CustomIterator:
    def __init__(self, max):
        self.max = max
        self.cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur < self.max:
            self.cur += 1
            return self.cur
        raise StopIteration


iterator = CustomIterator(3)  # <__main__.CustomIterator object at someAddressInMemory>
print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# Note: A generator is an iterator however, an iterator need not be a generator