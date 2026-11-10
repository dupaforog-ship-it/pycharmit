class MyIterator:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            self.i += 1
            return self.i
        raise StopIteration


obj = MyIterator(5)

for i in obj:
    print(i)