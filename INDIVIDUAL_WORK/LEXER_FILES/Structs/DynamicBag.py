<<<<<<< HEAD:INDIVIDUAL_WORK/LEXER_FILES/Structs/DynamicBag.py
from Structs.BagInterface import BagInterface
=======
import BagInterface
from abc import ABC
>>>>>>> 97b0ec7214dea84d30b6817131596f75cc4a7d89:JORGE/DynamicBag.py


class DynamicBag(BagInterface.BagInterface, ABC):
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


temp = DynamicBag()
temp.add('hi')
temp.add('hi')
temp.add('jose')
print(temp.elements)
print(temp.count('hi'))
print(temp.size())
print(temp.remove('jose'))
print(temp.removeAll('hi'))
print(temp.elements)
temp.add('go')
print(temp.elements)
temp.clear()
print(temp.elements)

<<<<<<< HEAD:INDIVIDUAL_WORK/LEXER_FILES/Structs/DynamicBag.py
    def clear(self):
        self.elements.clear()

def test():
    temo_bag = DynamicBag()
    temo_bag.add("hola")
    temo_bag.add("hola")
    temo_bag.add("hola")
    temo_bag.add("hola")
    temo_bag.add("hola")
    temo_bag.removeAll("hola")
=======
>>>>>>> 97b0ec7214dea84d30b6817131596f75cc4a7d89:JORGE/DynamicBag.py







