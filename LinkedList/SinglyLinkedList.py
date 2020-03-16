# Created by Andrew Gonzalez (GitHub: andrewgonzalez4) using Python and Vim as a text editor
# Defines the Node class in order to be able to create nodes and add them to the SLL.
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
#Defines the SinglyLinkedList class and its methods.
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.currentSize = 0
# The add method takes and item and adds it at the end of the list.
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

# The printList method prints the entire list in order.
    def printList(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

# The isEmpty method takes the list and checks if its empty.
    def isEmpty(self):
        if self.head is None:
           print("Empty")
        else:
            print("Not empty")

# The clear method takes the list and clears it.
    def clear(self):
        if self.head is None:
            return
        self.head = None
        self.currentSize = 0
        return

# The get method takes an index and returns the element at said position.
    def get(self, index):
        current = self.head
        position = 0
        if index >= self.currentSize:
            return
        while position != index:
            current = current.next
            position = position + 1
        print(current.data)

# The size method returns the size of the list.
    def size(self):
        print(self.currentSize)

# The removeLast method removes the element at the last index of the list.
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

