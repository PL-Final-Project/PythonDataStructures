from BinaryTreeNode import BinaryTreeNode
from KeyValuePair import KeyValuePair
from MapInterface import MapInterface
from SinglyLinkedList import SinglyLinkedList
from Comparator import Comparator


class BinarySearchTree(MapInterface):
    class Entry(KeyValuePair):

        def __init__(self, key, value):
            self.key = key
            self.value = value

        def getKey(self):
            return self.key

        def getValue(self):
            return self.value

        def setKey(self, key):
            self.key = key

        def setValue(self, value):
            self.value = value

    def __init__(self, keyComparator: Comparator):
        self.root = BinaryTreeNode
        self.root = None
        self.currentSize = 0
        self.keyComparator = keyComparator

    def size(self):
        return self.currentSize

    def isEmpty(self):
        return self.currentSize == 0

    def get(self, key):
        return self.getAux(key, self.root)

    def getAux(self, key, n):
        if n is None:
            return None
        comparison = self.keyComparator.compareTo(key, n.getValue().getKey())
        if comparison == 0:
            return n.getValue().getValue()
        elif comparison < 0:
            return self.getAux(key, n.getLeftChild())
        else:
            return self.getAux(key, n.getRightChild())

    def put(self, key, value):
        if self.root is None:
            entry = self.Entry(key, value)
            self.root = BinaryTreeNode(entry)
            self.currentSize = self.currentSize + 1
            return value
        return self.putAux(key, value, self.root)

    def putAux(self, key, value, n):
        comparison = self.keyComparator.compareTo(key, n.getValue().getKey())
        if comparison < 0:  # left
            if n.getLeftChild() is None:
                entry = self.Entry(key, value)
                newNode = BinaryTreeNode(entry, None, None, n)
                n.setLeftChild(newNode)
                self.currentSize = self.currentSize + 1
                return value
            else:
                return self.putAux(key, value, n.getLeftChild())
        else:
            if n.getRightChild() is None:
                entry = self.Entry(key, value)
                newNode = BinaryTreeNode(entry, None, None, n)
                n.setRightChild(newNode)
                self.currentSize = self.currentSize + 1
                return value
            else:
                return self.putAux(key, value, n.getRightChild())

    def remove(self, key):
        if self.root is None:
            return None
        else:
            comparison = self.keyComparator.compareTo(key, self.root.getValue().getKey())
            if comparison == 0:
                if self.isLeaf(self.root):
                    result = self.root.getValue().getValue()
                    self.root = None
                    self.currentSize = self.currentSize -1
                    return result
                elif self.root.getRightChild() is None:
                    result = self.root.getValue().getValue()
                    self.root = self.root.getLeftChild()
                    self.currentSize = self.currentSize - 1
                    return result
                else:
                    result = self.root.getValue().getValue()
                    s = self.smallestChild(self.root.getRightChild())
                    self.root.setValue(s.getValue())
                    self.removeAux(s.getValue().getKey(), self.root.getRightChild())
                    return result
            elif comparison < 0:
                return self.removeAux(key, self.root.getLeftChild())
            else:
                return self.removeAux(key, self.root.getRightChild())

    def isLeaf(self, n):
        return n.getLeftChild() is None and n.getRightChild() is None

    def removeAux(self, key, n):
        pass
     

    def smallestChild(self, n):
        temp = n
        while temp.getLeftChild() is not None:
            temp = temp.getLeftChild()
        return temp

    def makeEmpty(self):
        self.root = None
        self.root.setRightChild = None
        self.root.setLeftChild = None
        return

    def containsKey(self, key):
        return self.get(key) is not None

    def getKeys(self):
        result = SinglyLinkedList()
        self.getKeysAux(self.root, result)
        return result

    def getKeysAux(self, n, result):
        if n is None:
            return
        else:
            self.getKeysAux(n.getLeftChild(), result)
            result.add(n.getValue().getKey())
            self.getKeysAux(n.getRightChild(), result)

    def getValues(self):
        result = SinglyLinkedList()
        self.getValuesAux(self.root, result)
        return result

    def getValuesAux(self, n, result):
        if n is None:
            return
        else:
            self.getValuesAux(n.getLeftChild(), result)
            result.add(n.getValue().getValue())
            self.getValuesAux(n.getRightChild(), result)

