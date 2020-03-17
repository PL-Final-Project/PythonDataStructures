import math
import random

from MapInterface import MapInterface
from MapEntry import MapEntry
from SinglyLinkedList import SinglyLinkedList


class HashTableOA(MapInterface):

    def __init__(self, size=10, keyComparator=None, valueComparator=None):
        """
        :type keyComparator: object
        :type valueComparator: object
        :type size: int
        """
        self.buckets = [MapEntry()] * size
        self.currentSize = 0
        self.keyComparator = keyComparator
        self.valueComparator = valueComparator

    def linearHashFunction(self, key, array) -> int:
        return int(hash(key) % len(array))

    def squareHashFunction(self, key, array) -> int:
        return int((math.pow(hash(key), 2)) % len(array))

    def cubicHashFunction(self, key, array) -> int:
        return int((math.pow(hash(key), 3)) % len(array))

    def size(self) -> int:
        return self.currentSize

    def isEmpty(self) -> bool:
        return self.size() == 0

    def get(self, key) -> object:
        result = None
        # --------------------------------------
        # We hash to the first possible location
        firstPosition = self.linearHashFunction(key, self.buckets)
        # We acquire the first object in said hash position
        elementFirstPosition = self.buckets[firstPosition]
        if elementFirstPosition.isStatus() is True and elementFirstPosition.getKey() is key:
            result = elementFirstPosition.getValue()
            return result
        # ---------------------------------------
        # If first hash doesn't return proceed to hash again
        secondPosition = self.squareHashFunction(key, self.buckets)
        # We acquire the first object in second hash position
        elementSecondPosition = self.buckets[secondPosition]
        if elementSecondPosition.isStatus() is True and elementSecondPosition.getKey() is key:
            result = elementSecondPosition.getValue()
            return result
        # ---------------------------------------
        # If second hash doesn't return proceed to hash again
        thirdPosition = self.cubicHashFunction(key, self.buckets)
        # We acquire the first object in third hash position
        elementThirdPosition = self.buckets[thirdPosition]
        if elementThirdPosition.isStatus() is True and elementThirdPosition.getKey() is key:
            result = elementThirdPosition.getValue()
            return result
        # ---------------------------------------
        # If it fails to get object in third hash we proceed to probe in linear fashion
        tempIndex = (self.linearHashFunction(key, self.buckets) + 1) % len(self.buckets)
        while tempIndex != self.linearHashFunction(key, self.buckets):
            if self.buckets[tempIndex].isStatus() is True and self.buckets[tempIndex].getKey() is key:
                result = self.buckets[tempIndex].getValue()
                return result
            tempIndex = (tempIndex + 1) % len(self.buckets)
        return result

    def put(self, key, value) -> bool:
        # We first create the object to be added into the table and initialize final index position
        newEntry = MapEntry(key, value, True)
        # We first check if it exists on the the table
        # OPTIONAL - IF DESIRED WE CAN RESTRICT THE LIST TO ONLY
        # ACCEPT ELEMENTS THAT ARE NOT ALREADY IN HASH TABLE
        if self.containsKey(key):
            self.remove(key)
        # Check if percentage of elements is below 50% of capacity
        if (self.currentSize / len(self.buckets)) >= 0.5:
            # if its over half capacity, extend array (WORST CASE SCENARIO)
            self.__reallocate()
        # ---------------------------------------
        # We begin by first locating first  hashing position
        firstFreePosition = self.linearHashFunction(key, self.buckets)
        entryIndex = firstFreePosition
        if self.buckets[entryIndex] is not None and self.buckets[entryIndex].isStatus() is not False:
            # ---------------------------------------
            # If first hashing position fails we proceed to second hash
            secondFreePosition = self.squareHashFunction(key, self.buckets)
            entryIndex = secondFreePosition
            if self.buckets[entryIndex] is not None and self.buckets[entryIndex].isStatus() is not False:
                # ---------------------------------------
                # If second hashing position fails we proceed to second hash
                thirdFreePosition = self.cubicHashFunction(key, self.buckets)
                entryIndex = thirdFreePosition
                if self.buckets[entryIndex] is not None and self.buckets[entryIndex].isStatus() is not False:
                    # ---------------------------------------
                    # If third hash fails we proceed to linear probing
                    tempIndex = (self.linearHashFunction(key, self.buckets) + 1) % len(self.buckets)
                    while tempIndex != self.linearHashFunction(key, self.buckets):
                        # If empty space is found then set index to such spot
                        if self.buckets[tempIndex] is not None and self.buckets[tempIndex].isStatus() is False:
                            entryIndex = tempIndex
                            break
                        tempIndex = (tempIndex + 1) % len(self.buckets)
        self.buckets[entryIndex] = newEntry
        self.currentSize += 1
        return True

    # Private method
    def __reallocate(self):
        temporalSize = len(self.buckets) * 2
        temp = HashTableOA(temporalSize, self.keyComparator, self.valueComparator)
        for element in self.buckets:
            if element is not None and element.isStatus() is True:
                temp.put(element.getKey(), element.getValue())
        self.buckets = temp.buckets

    def remove(self, key) -> object:
        # We begin search of the element with first hash functions
        firstPosition = self.linearHashFunction(key, self.buckets)
        eliminateIndex = firstPosition
        firstElement = self.buckets[firstPosition]
        if firstElement.isStatus() is False or firstElement.getKey() is not key:
            # If first hashing fails proceed to second hashing
            secondPosition = self.squareHashFunction(key, self.buckets)
            secondElement = self.buckets[secondPosition]
            eliminateIndex = secondPosition
            if secondElement.isStatus() is False or secondElement.getKey() is not key:
                # If first hashing fails proceed to second hashing
                thirdPosition = self.cubicHashFunction(key, self.buckets)
                thirdElement = self.buckets[thirdPosition]
                eliminateIndex = thirdPosition
                if thirdElement.isStatus() is False or thirdElement.getKey() is not key:
                    # If third hashing fails we proceed into linear probing
                    tempIndex = (self.linearHashFunction(key, self.buckets) + 1) % len(self.buckets)
                    while tempIndex != self.linearHashFunction(key, self.buckets):
                        # If specified loc
                        if self.buckets[tempIndex].isStatus() is True and self.buckets[tempIndex].getKey() is key:
                            eliminateIndex = tempIndex
                            break
                        tempIndex = (tempIndex + 1) % len(self.buckets)
                # if linear probe fails the object doesn't exist
                if tempIndex == self.linearHashFunction(key, self.buckets):
                    return None
        result = self.buckets[eliminateIndex].getValue()
        self.buckets[eliminateIndex] = MapEntry()
        self.currentSize -= 1
        return result

    def makeEmpty(self):
        tempIndex = 0
        while tempIndex < len(self.buckets):
            self.buckets[tempIndex] = MapEntry()
            tempIndex += 1
        self.currentSize = 0

    def containsKey(self, key) -> bool:
        return self.get(key) is not None

    def getKeys(self):
        result = SinglyLinkedList()
        # the result will be a list with all the keys
        for element in self.buckets:
            if element is not None and element.isStatus() is True:
                result.add(element.getKey())
        return result

    def getValues(self):
        result = SinglyLinkedList()
        # the result will be a list with all the values
        for element in self.buckets:
            if element is not None and element.isStatus() is True:
                result.add(element.getValue())
        return result


# TESTING
def main():
    t = HashTableOA(8)
    t.put("var1", 1)
    t.put("var2", 1)
    t.put("var3", 1)
    t.put("var4", 1)
    t.put("var5", 1)
    t.put("var9", 1)
    t.put("var6", 1)
    t.put("var7", 1)
    t.put("var8", 1)
    print(t.get("var1"))
    t.makeEmpty()


def thousandCases():
    testing = HashTableOA(20)
    letters = ["A", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]
    for num in range(999):
        temp = ""
        for numbers in range(6):
            temp += letters[random.randint(0, len(letters) - 1)]
        testing.put(temp, num)
    allkeys = testing.getKeys()
    testing.makeEmpty()


if __name__ == '__main__':
    # main()
    thousandCases()
