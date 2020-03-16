class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.currentSize = 0

    def add(self, newItem):
        if newItem is None:
            return
        NewNode = Node(newItem)
        if self.head is None:
            self.head = NewNode
            self.currentSize = self.currentSize + 1
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = NewNode
        self.currentSize = self.currentSize + 1

    def printList(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def isEmpty(self):
        if self.head is None:
           print("Empty")
        else:
            print("Not empty")

    def clear(self):
        if self.head is None:
            return
        self.head = None
        self.currentSize = 0
        return

    def get(self, index):
        current = self.head
        position = 0
        if index >= self.currentSize:
            return
        while position != index:
            current = current.next
            position = position + 1
        print(current.data)

    def size(self):
        print(self.currentSize)

    def removeLast(self):
       if self.head == None: 
        return None
       if self.head.next == None: 
        self.head = None
        self.currentSize = self.currentSize - 1
        return None
       second_last = self.head 
       while(second_last.next.next): 
        second_last = second_last.next
       second_last.next = None
       self.currentSize = self.currentSize - 1
       return self.head  

list = LinkedList()
list.add("Andrew")
list.add("Francisco")
list.add("Jorge")
list.add("Alberto")
list.get(2)
