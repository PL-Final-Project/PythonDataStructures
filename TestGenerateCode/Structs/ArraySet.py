from Structs.SetInterface import SetInterface


class ArraySet(SetInterface):

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
        for item in self.elements:
            self.elements.remove(item)

    def isSubset(self, newdata: SetInterface):
        for i in newdata:
            if not newdata.isMember(self.elements[i]):
                return False

        return True

    def union(self, newdata: SetInterface):
        result = ArraySet()
        for item in self.elements:
            if not newdata.isMember(item):
                result.add(item)

        return result

    def difference(self, newdata: SetInterface):
        result = ArraySet()
        for item in self.elements:
            if not newdata.isMember(item):
                result.add(item)

        return result

    def intersection(self, newdata: SetInterface):
        return self.difference(self.difference(newdata))

    def toArray(self):
        return self.elements
