from Structs.Comparator import Comparator
from Structs.ListInterface import SortedListInterface as Interface
from Structs.StringComparator import StringComparator


class SortedArrayList(Interface):

    def __init__(self, comparator: Comparator, size=10):
        self.__currentSize = 0
        self.elements = [None] * size
        self.__comparator = comparator

    def size(self):
        return self.__currentSize

    def isEmpty(self):
        return self.size() == 0

    def clear(self):
        tempIndex = 0
        while tempIndex < len(self.elements):
            self.elements[tempIndex] = None
            tempIndex += 1
        self.__currentSize = 0
        return

    def get_obj(self, obj):
        index = self.firstIndexOf(obj)
        if index != 1:
            return self.get_index(index)
        return None

    def get_index(self, index):
        try:
            return self.elements[index]
        except IndexError as error:
            print("IndexOutOFBounds")
            return None

    def add(self, obj):
        if self.size() > len(self.elements) - 1:
            self.__reAllocate()
        tempIndex = 0
        while tempIndex < len(self.elements):
            elementB = self.elements[tempIndex]
            if elementB is None:
                self.elements[tempIndex] = obj
                self.__currentSize += 1
                return
            elif self.__comparator.compareTo(obj, elementB) < 0:
                subIndex = self.__currentSize
                while subIndex > tempIndex:
                    if self.elements[subIndex - 1] is not None:
                        self.elements[subIndex] = self.elements[subIndex - 1]
                    subIndex -= 1
                self.elements[tempIndex] = obj
                self.__currentSize += 1
                return
            tempIndex += 1

    def __reAllocate(self):
        temp = SortedArrayList(self.__comparator, len(self.elements) * 2)
        for element in self.elements:
            if element is not None:
                temp.add(element)
        self.elements = temp.elements

    def remove_obj(self, obj):
        index = self.firstIndexOf(obj)
        if index != -1:
            self.remove_index(index)
            return True
        return False

    def remove_index(self, index):
        try:
            self.elements[index] = None
            if index < len(self.elements):
                tempIndex = index + 1
                while tempIndex < len(self.elements):
                    self.elements[tempIndex - 1] = self.elements[tempIndex]
                    tempIndex += 1
            self.elements[len(self.elements) - 1] = None
            self.__currentSize -= 1
            return True
        except IndexError as error:
            print(error)
            return False

    def isMember(self, obj):
        return self.get_obj(obj) is None

    def firstIndexOf(self, obj):
        tempIndex = 0
        while tempIndex < len(self.elements):
            element = self.elements[tempIndex]
            if element is obj:
                return tempIndex
            tempIndex += 1
        return -1

    def lastIndexOf(self, obj):
        tempIndex = len(self.elements) - 1
        while tempIndex > -1:
            element = self.elements[tempIndex]
            if element is obj:
                return tempIndex
            tempIndex -= 1
        return -1

    def printValues(self):
        for element in self.elements:
            if element is not None:
                print(element)


def main():
    list1 = SortedArrayList(StringComparator(), 2)
    list1.add("Hola")
    list1.add("Adios")
    list1.add("Berto")
    list1.add("Dio")
    list1.add("Carlos")
    list1.remove_index(8)
    list1.remove_obj("Carlos")
    list1.remove_obj("Dio")


if __name__ == '__main__':
    main()
