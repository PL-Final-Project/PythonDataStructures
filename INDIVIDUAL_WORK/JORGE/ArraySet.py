import SetInterface
from abc import ABC


class ArraySet(SetInterface.SetInterface, ABC):

    def __init__(self):
        self.elements = []
        self.default_size = 10

    def size(self):
        return len(self.elements)

    def isEmpty(self):
        return len(self.elements) == 0

    def add(self, item):
        if item not in self.elements:
            self.elements.append(item)
        else:
            return "item already in set"

    def isMember(self, item):
        return item in self.elements

    def remove(self, item):
        self.elements.remove(item)
        return True

    def clear(self):
        while not self.isEmpty():
            self.remove(self.elements[0])

    def isSubset(self, data):
        for i in range(0, self.size()):
            if not data.isMember(self.elements[i]):
                return False

        return True

    def union(self, data):
        result = []
        for i in self.elements:
            result.append(i)

        temp = data.toArray()
        for i in range(0, data.size()):
            if not temp[i] in result:
                result.append(temp[i])

        final = ArraySet()
        for i in result:
            final.add(i)

        return final

    def difference(self, data):
        result = []
        for i in self.elements:
            if not data.isMember(i):
                result.append(i)

        final = ArraySet()
        for i in result:
            final.add(i)

        return final

    def intersection(self, data):
        return self.difference(self.difference(data))

    def toArray(self):
        result = []
        for i in self.elements:
            result.append(i)

        return result


temp = ArraySet()
temp_2 = ArraySet()
temp.add('hi')
temp.add('nigga')
temp.add('apu')
temp_2.add('hi')
temp_2.add('nigga')
temp_2.add('joe')
temp_3 = temp_2.difference(temp).elements
temp_4 = temp.intersection(temp_2).elements


print(temp.elements)
print(temp_2.elements)
print(temp_3)
print(temp_4)
