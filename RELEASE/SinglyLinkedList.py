# Created by Andrew Gonzalez (GitHub: andrewgonzalez4) using Python and Vim as a text editor
# Defines the Node class in order to be able to create nodes and add them to the SLL.
import release_parser

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Defines the SinglyLinkedList class and its methods.
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.currentSize = 0

    # The add method takes and item and adds it at the end of the list.
    def add(self, newItem):
        if newItem is None:
            return False
        NewNode = Node(newItem)
        if self.head is None:
            self.head = NewNode
            self.currentSize = self.currentSize + 1
            return True
        last = self.head
        while last.next:
            last = last.next
        last.next = NewNode
        self.currentSize = self.currentSize + 1

    # The printList method prints the entire list in order.
    def display(self):
        printval = self.head
        while printval is not None:
            release_parser.messages.append(printval.data)
            printval = printval.next

    # The isEmpty method takes the list and checks if its empty.
    def isEmpty(self):
        if self.head is None:
            # print("Empty")
            return True
        else:
            # print("Not empty")
            return False

    # The clear method takes the list and clears it.
    def clear(self):
        if self.head is None:
            return
        self.head = None
        self.currentSize = 0
        return

    def contains(self, element):
        temp = self.head
        while temp is not None:
            if temp.data == element:
                return True
            temp = temp.next
        return False

    def remove(self,value):
        if self.contains(value):
            prev = None
            curr = self.head
            while curr:
                if curr.data == value:
                    if prev:
                        prev.next = curr.next
                    else:
                        self.head = curr.next
                    self.currentSize-=1
                    return True
                prev = curr
                curr = curr.next
        return False
            
        return False
    # The get method takes an index and returns the element at said position.
    def get(self, index):
        current = self.head
        position = 0
        if index >= self.currentSize:
            return
        while position != index:
            current = current.next
            position = position + 1
        return current.data

    # The size method returns the size of the list.
    def size(self):
        return self.currentSize

    # The removeLast method removes the element at the last index of the list.
    def removeLast(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            self.currentSize = self.currentSize - 1
            return None
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None
        self.currentSize = self.currentSize - 1
        return self.head

