class TakeSkip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        number = self.number
        if self.count > 0:
            self.number += 1
            self.count -= 1
            return number * self.step
        raise StopIteration


numbers = TakeSkip(2, 6)
for number in numbers:
    print(number)

