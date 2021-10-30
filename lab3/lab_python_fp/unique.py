from gen_random import gen_random

class Unique(object):
    def __init__(self, items, ignore_case=False):
        self.used_items = set()
        self.items = list(items)
        self.index = 0
        self.ignore_case = ignore_case

    def __next__(self):
        while True:
            if self.index >= len(self.items):
                raise StopIteration
            else:
                current = self.items[self.index]
                self.index += 1
                if self.ignore_case:
                    if current.lower() not in self.used_items:
                        self.used_items.add(current.lower())
                        return current
                elif current not in self.used_items:
                    self.used_items.add(current)
                    return current

    def __iter__(self):
        return self


if __name__ == '__main__':
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for el in Unique(data):
        print(el)

    data = gen_random(10, 1, 3)
    for el in Unique(data):
        print(el)

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for el in Unique(data):
        print(el)

    for el in Unique(data, ignore_case=True):
        print(el)
