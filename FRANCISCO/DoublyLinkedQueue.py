from abc import ABC

from .QueueInterface import QueueInterface

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedQueue(QueueInterface, ABC):

    def __init__(self):
        self.currentSize = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def size(self):
        return self.currentSize

    def isEmpty(self):
        if self.currentSize == 0:
            return True
        return False

    def front(self):
        if self.isEmpty():
            return None
        return self.head.next.data

    def dequeue(self):
        if self.isEmpty():
            return None
        target = self.head.next
        result = target.data
        self.head.next = target.next
        target.next.prev = self.head
        target.next = None
        target.prev = None
        target.data = None
        self.currentSize = self.currentSize - 1
        return result

    def enqueue(self, newdata):
        newNode = Node(newdata)
        newNode.prev = self.tail.prev
        newNode.next = self.tail
        self.tail.prev = newNode
        newNode.prev.next = newNode
        self.currentSize = self.currentSize + 1
        return

    def makeEmpty(self):
        while self.dequeue() is not None:
            x = 0
        return






