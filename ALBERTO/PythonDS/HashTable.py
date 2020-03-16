from Map import MapInterface
import math


class MapEntry:
    def __init__(self, key=None, value=None, status=False):
        self.key = key
        self.value = value
        self.status = status

    def isStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value


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

    def linearHashFunction(self, key, arraySize) -> int:
        return int(hash(key) % arraySize)

    def squareHashFunction(self, key, arraySize) -> int:
        return int((math.pow(hash(key), 2)) % arraySize)

    def size(self) -> int:
        return self.currentSize

    def isEmpty(self) -> bool:
        return self.size() == 0

    def get(self, key) -> object:
        result = None
        # --------------------------------------
        # We hash to the first possible location
        firstPosition = self.linearHashFuntion(key, len(self.buckets))
        # We acquire the first object in said hash position
        elementFirstPosition = self.buckets[firstPosition]
        if elementFirstPosition is not None and elementFirstPosition.getKey() is key:
            result = elementFirstPosition.getValue()
            return result
        # ---------------------------------------
        # If first hash doesn't return proceed to hash again
        secondPosition = self.squareHashFuntion(key, len(self.buckets))
        # We acquire the first object in second hash position
        elementSecondPosition = self.buckets[secondPosition]
        if elementSecondPosition is not None and elementSecondPosition.getKey() is key:
            result = elementSecondPosition.getValue()
            return result
        # ---------------------------------------
        # If it fails to get object in second hash we proceed to probe in linear fashion
        tempIndex = (self.linearHashFuntion(key, len(self.buckets)) + 1) % len(self.buckets)
        while tempIndex != self.linearHashFuntion(key, len(self.buckets)):
            if self.buckets[tempIndex] is not None and self.buckets[tempIndex].getKey() is key:
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
        firstFreePosition = self.linearHashFuntion(key, len(self.buckets))
        entryIndex = firstFreePosition
        if self.buckets[entryIndex] is not None or self.buckets[entryIndex].getKey() is not key:
            # ---------------------------------------
            # If first hashing position fails we proceed to second hash
            secondFreePosition = self.squareHashFuntion(key, len(self.buckets))
            entryIndex = secondFreePosition
            if self.buckets[entryIndex] is not None or self.buckets[entryIndex].getKey() is not key:
                # ---------------------------------------
                # If second hash fails we proceed to linear probing
                tempIndex = (self.linearHashFuntion(key, len(self.buckets)) + 1) % len(self.buckets)
                while tempIndex != self.linearHashFuntion(key, len(self.buckets)):
                    # If empty space is found then set index to such spot
                    if self.buckets[tempIndex] is None:
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
            if element is not None and element.getStatus() is True:
                temp.put(element.getKey(), element.getValue())
        self.buckets = temp.buckets

    def remove(self, key) -> object:
        # We begin search of the element with first hash functions
        firstPosition = self.linearHashFunction(key, len(self.buckets))
        eliminateIndex = firstPosition
        firstElement = self.buckets[firstPosition]
        if firstElement is None or firstElement.getKey() is not key:
            # If first hashing fails proceed to second hashing
            secondPosition = self.squareHashFunction(key, len(self.buckets))
            secondElement = self.buckets[secondPosition]
            eliminateIndex = secondPosition
            if secondElement is None or secondElement.getKey() is not key:
                # If second hashing fails we proceed into linear probing
                tempIndex = (self.linearHashFuntion(key, len(self.buckets)) + 1) % len(self.buckets)
                while tempIndex != self.linearHashFuntion(key, len(self.buckets)):
                    # If specified loc
                    if self.buckets[tempIndex] is not None and self.buckets[tempIndex].getKey() is key:
                        eliminateIndex = tempIndex
                        break
                    tempIndex = (tempIndex + 1) % len(self.buckets)
                # if linear probe fails the object doesn't exist
                if tempIndex == self.linearHashFuntion(key, len(self.buckets)):
                    return None
        result = self.buckets[eliminateIndex]
        self.buckets[eliminateIndex] = MapEntry()
        self.currentSize -= 1
        return result

    def makeEmpty(self):
        tempIndex = 0
        while tempIndex < len(self.buckets):
            self.buckets[tempIndex] = MapEntry()
        self.currentSize = 0

    def containsKey(self, key) -> bool:
        return self.get(key) is not None

    def getKeys(self):
        pass

    def getValues(self):
        pass


def main():
    print("Hello")
    t = HashTableOA()
    t.put("var1", 1)
    print(t.get("var1"))


if __name__ == '__main__':
    main()
