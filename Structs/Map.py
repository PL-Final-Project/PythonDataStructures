from Structs import (MapInterface,SinglyLinkedList,MapEntry)



class Map(MapInterface.MapInterface):
    def __init__(self):
        self.__elements = SinglyLinkedList.SinglyLinkedList()
        self.__currentSize = 0

    def size(self):
        return self.__elements.size()

    def isEmpty(self):
        return self.size() != 0

    def get(self, key):
        tempIndex = 0
        while tempIndex < self.__elements.size():
            element = self.__elements.get(tempIndex)
            if element is not None and element.isStatus() is True and element.getKey() == key:
                return element.getValue()
            tempIndex += 1
        return None

    def put(self, key, value):
        if self.containsKey(key) is True:
            self.remove(key)
        self.__elements.add(MapEntry.MapEntry(key, value, True))
        return

    def remove(self, key):
        result = None
        tempIndex = 0
        while tempIndex < self.__elements.size():
            element = self.__elements.get(tempIndex)
            if element is not None and element.isStatus() is True and element.getKey() == key:
                result = element.getValue()
                self.__elements.remove(element)
                return result
            tempIndex += 1
        return result

    def makeEmpty(self):
        self.__elements.clear()
        self.__currentSize = 0

    def containsKey(self, key):
        return self.get(key) is not None

    def getKeys(self):
        result = SinglyLinkedList.SinglyLinkedList()
        tempIndex = 0
        while tempIndex < self.__elements.size():
            element = self.__elements.get(tempIndex)
            if element is not None and element.isStatus() is True:
                result.add(element.getKey())
            tempIndex += 1
        return result

    def getValues(self):
        result = SinglyLinkedList.SinglyLinkedList()
        tempIndex = 0
        while tempIndex < self.__elements.size():
            element = self.__elements.get(tempIndex)
            if element is not None and element.isStatus() is True:
                result.add(element.getValue())
            tempIndex += 1
        return result
