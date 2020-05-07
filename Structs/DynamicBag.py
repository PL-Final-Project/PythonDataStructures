import Structs.BagInterface
from abc import ABC


class DynamicBag:
    def __init__(self):
        self.elements = []
        self.default_size = 10

    def size(self):
        return len(self.elements)

    def isEmpty(self):
        return len(self.elements) == 0

    def add(self, item):
        self.elements.append(item)

    def isMember(self, item):
        return item in self.elements

    def count(self, item):
        result = 0
        for i in range(0, len(self.elements)):
            if self.elements[i] == item:
                result += 1
        return result

    def remove(self, item):
        self.elements.remove(item)
        return True

    def removeAll(self, item):
        result = 0
        while self.isMember(item):
            self.elements.remove(item)
            result += 1
        return 'removed {0} '.format(result)
    def clear(self):
        while not self.isEmpty():
            self.remove(self.elements[0])










