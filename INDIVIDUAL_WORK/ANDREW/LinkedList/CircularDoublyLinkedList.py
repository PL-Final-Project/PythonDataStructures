from SinglyLinkedList import Node

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.first = None
 
    def get_node(self, index):
        current = self.first
        for i in range(index):
            current = current.next
            if current == self.first:
                return None
        return current
 
    def insert_after(self, ref_node, new_node):
        new_node.prev = ref_node
        new_node.next = ref_node.next
        new_node.next.prev = new_node
        ref_node.next = new_node
 
    def insert_before(self, ref_node, new_node):
        self.insert_after(ref_node.prev, new_node)
 
    def insert_at_end(self, new_node):
        if self.first is None:
            self.first = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.insert_after(self.first.prev, new_node)
 
    def insert_at_beg(self, new_node):
        self.insert_at_end(new_node)
        self.first = new_node
 
    def remove(self, node):
        if self.first.next == self.first:
            self.first = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if self.first == node:
                self.first = node.next
    def display(self):
        if self.first is None:
            return
        current = self.first
        while True:
            print(current.data, end = ' ')
            current = current.next
            if current == self.first:
                break  

list = CircularDoublyLinkedList()
n1 = Node("Melanie")
n2 = Node("Andrew")
n3 = Node("Ronaldo")
n4 = Node("Mister")
list.insert_at_beg(n1)
list.insert_at_beg(n2)
list.insert_at_end(n4)
list.insert_at_end(n3)
list.display()
