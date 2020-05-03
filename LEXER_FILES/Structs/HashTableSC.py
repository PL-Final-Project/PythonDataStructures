import random

from MapInterface import MapInterface
from MapEntry import MapEntry
from Sorted.Comparator import Comparator
from Sorted.StringComparator import StringComparator
from Sorted.NumberComparator import NumberComparator
from Sorted.SortedArrayList import SortedArrayList
from SinglyLinkedList import SinglyLinkedList


class HashTableSC(MapInterface):
    def __init__(self, size: int = 10, keyComparator: Comparator = None, valueComparator: Comparator = None):
        self.buckets = [None] * size
        firstTempIndex: int = 0
        while firstTempIndex < size:
            self.buckets[firstTempIndex] = SinglyLinkedList()
            firstTempIndex += 1
        self.currentSize = 0
        self.keyComparator = keyComparator
        self.valueComparator = valueComparator

    def size(self) -> int:
        return self.currentSize

    def isEmpty(self) -> bool:
        return self.size() == 0

    def linearHashFunction(self, key, array) -> int:
        return int(hash(key) % len(array))

    def get(self, key) -> object:
        # To begin the search, we must first use the hash function to determine first location
        firstElementPosition = self.linearHashFunction(key, self.buckets)
        firstList = self.buckets[firstElementPosition]
        # We acquire a list and start traversing through it until we find the element
        tempIndex = 0
        while tempIndex < firstList.size():
            element = firstList.get(tempIndex)
            if element.isStatus() is True and element.getKey() is key:
                return element.getValue()
            tempIndex += 1
        """
        This code below would be detrimental to the performance of the hash table. We assume that it can always
        be found in the first hashing position, maybe not on index 0 of the linked list but close enough to reduce
        the complexity to a worst case scenario of  O(N) (N being the size of the linked list) and not a O(N*M*P*Q*...)
        """
        # If not found on designated list, check on all lists
        # index_1 = 0
        # while index_1 < len(self.buckets):
        #     index_2 = 0
        #     currList = self.buckets[index_1]
        #     while index_2 < currList.size():
        #         visibleElement = currList.get(index_2)
        #         if visibleElement.isStatus() is True and visibleElement.getKey() is True:
        #             return visibleElement.getValue()
        #         index_2 += 1
        #     index_1 += 1

        # If element is not on any list it doesn't exist
        return None

    def put(self, key, value):
        # Creation of new element to be included in Hash Table
        newEntry = MapEntry(key, value, True)
        # Check if element doesn't exist
        if self.containsKey(key) is True:
            # if it does exist delete
            self.remove(key)
        # We check if the existing ratio between elements and spaces hasn't surpassed 70%
        if self.size() / len(self.buckets) >= 0.7:
            # if surpassed reAllocate the hash table
            self.__reAllocate()
        # To know corresponding location, we hash it first
        firstElementPosition = self.linearHashFunction(key, self.buckets)
        firstList = self.buckets[firstElementPosition]
        # We add it to the list
        firstList.add(newEntry)
        self.currentSize += 1
        return True

    def __reAllocate(self):
        tempHashTable = HashTableSC(len(self.buckets) * 2, self.keyComparator, self.valueComparator)
        for lists in self.buckets:
            if lists is not None and lists.size() != 0:
                tempIndex = 0
                while tempIndex < lists.size():
                    element = lists.get(tempIndex)
                    if element is not None:
                        tempHashTable.put(element.getKey(), element.getValue())
                    tempIndex += 1
        self.buckets = tempHashTable.buckets

    def remove(self, key):
        result = None
        # To begin deleting we must first search for its hashing position
        firstElementPosition = self.linearHashFunction(key, self.buckets)
        firstList = self.buckets[firstElementPosition]
        # We traverse to the list and we find the element
        tempIndex = 0
        while tempIndex < firstList.size():
            element = firstList.get(tempIndex)
            if element is not None and element.isStatus() is True and element.getKey() is key:
                result = element.getValue()
                firstList.remove(tempIndex)
                self.currentSize -= 1
                break
            tempIndex += 1
        # if not found it will return None
        return result

    def makeEmpty(self):
        tempIndex: int = 0
        while tempIndex < len(self.buckets):
            self.buckets[tempIndex] = SinglyLinkedList()
            tempIndex += 1
        self.currentSize = 0

    def containsKey(self, key):
        return self.get(key) is not None

    def getKeys(self):
        # The method returns a list with all the keys
        result = SinglyLinkedList()
        for lists in self.buckets:
            if lists is not None:
                tempIndex = 0
                while tempIndex < lists.size():
                    element = lists.get(tempIndex)
                    if element is not None and element.isStatus() is True:
                        result.add(element.getKey())
                    tempIndex += 1
        return result

    def getValues(self):
        # The method returns a list with all the values
        result = SinglyLinkedList()
        for lists in self.buckets:
            if lists is not None:
                tempIndex = 0
                while tempIndex < lists.size():
                    element = lists.get(tempIndex)
                    if element is not None and element.isStatus() is True:
                        result.add(element.getValue())
                    tempIndex += 1
        return result

    def getSortedKeys(self):
        # The method returns a list with all the keys
        result = SortedArrayList(self.keyComparator)
        for lists in self.buckets:
            if lists is not None:
                tempIndex = 0
                while tempIndex < lists.size():
                    element = lists.get(tempIndex)
                    if element is not None and element.isStatus() is True:
                        result.add(element.getKey())
                    tempIndex += 1
        return result

    def getSortedValues(self):
        # The method returns a list with all the values
        result = SortedArrayList(self.valueComparator)
        for lists in self.buckets:
            if lists is not None:
                tempIndex = 0
                while tempIndex < lists.size():
                    element = lists.get(tempIndex)
                    if element is not None and element.isStatus() is True:
                        result.add(element.getValue())
                    tempIndex += 1
        return result


def main():
    t = HashTableSC(2)
    t.put("var1", 1)
    t.put("var2", 1)
    t.put("var3", 1)
    t.remove("var3")
    print(t.get("var1"))
    t.makeEmpty()


def thousandCases():
    testing = HashTableSC(10,StringComparator(), NumberComparator())
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z"]
    for num in range(999):
        temp = ""
        for numbers in range(26):
            temp += letters[random.randint(0, len(letters) - 1)]
        testing.put(temp, num)
    allValues = testing.getSortedKeys()
    print(allValues.size())
    allValues.printValues()
    allValues.printValues()
    testing.makeEmpty()


if __name__ == '__main__':
    thousandCases()
