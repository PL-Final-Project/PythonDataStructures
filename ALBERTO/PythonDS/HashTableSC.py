from Map import MapInterface
from SinglyLinkedList import SinglyLinkedList


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


class HashTableSC(MapInterface):
    def __init__(self, size=10, keyComparator=None, valueComparator=None):
        self.buckets = [None] * size
        firstTempIndex = 0
        while firstTempIndex < size:
            self.buckets[firstTempIndex] = SinglyLinkedList()
            firstTempIndex += 1
        self.currentSize = 0
        self.keyComparator = keyComparator
        self.valueComparator = valueComparator

    def size(self) -> int:
        return self.currentSize

    def isEmpty(self) -> bool:
        return self.size() != 0

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
        # If element is not on the list it doesn't exist
        return None

    def put(self, key, value):
        # Creation of new element to be included in Hash Table
        newEntry = MapEntry(key, value, True)
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
            tempIndex += 1
        # if not found it will return None
        self.currentSize -= 1
        return result

    def makeEmpty(self):
        tempIndex = 0
        while tempIndex < len(self.buckets):
            self.buckets[tempIndex] = SinglyLinkedList()
            tempIndex += 1
        self.currentSize = 0

    def containsKey(self, key):
        return self.get(key) is not None

    def getKeys(self):
        # The method returns a list with all the keys
        result = SinglyLinkedList
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
        result = SinglyLinkedList
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


if __name__ == '__main__':
    main()
