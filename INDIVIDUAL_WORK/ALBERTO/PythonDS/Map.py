from MapInterface import MapInterface
from MapEntry import MapEntry
from SinglyLinkedList import SinglyLinkedList


class Map(MapInterface):
    def __init__(self):
        self.__elements = SinglyLinkedList()
        self.__currentSize = 0

    def size(self):
        return self.__elements.size()

    def isEmpty(self):
        return self.size() != 0

    def get(self, key):
        tempIndex = 0
        while tempIndex < self.__elements.size():
            element = self.__elements.get(tempIndex)
            if element is not None and element.isStatus() is True and element.getKey() is key:
                return element.getValue()
        return None

    def put(self, key, value):
        if self.containsKey(key) is True:
            self.remove(key)
        self.__elements.add(MapEntry(key, value, True))
        return True

    def remove(self, key):
        result = None
        tempIndex = 0
        while tempIndex < self.__elements.size():
            element = self.__elements.get(tempIndex)
            if element is not None and element.isStatus() is True and element.getKey() is key:
                result = element.getValue()
                self.__elements.remove(tempIndex)
                return result
        return result

    def makeEmpty(self):
        self.__elements.clear()
        self.__currentSize = 0

    def containsKey(self, key):
        return self.get(key) is not None

    def getKeys(self):
        result = SinglyLinkedList()
        tempIndex = 0
        while tempIndex < self.__elements.size():
            element = self.__elements.get(tempIndex)
            if element is not None and element.isStatus() is True:
                result.add(element.getKey())
            tempIndex += 1
        return result

    def getValues(self):
        result = SinglyLinkedList()
        tempIndex = 0
        while tempIndex < self.__elements.size():
            element = self.__elements.get(tempIndex)
            if element is not None and element.isStatus() is True:
                result.add(element.getValue())
            tempIndex += 1
        return result
