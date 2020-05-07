from Structs.SinglyLinkedList import Node

class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
       self.prev = None
 
 
class CircularDoublyLinkedList:
    def __init__(self):
        self.first = None
        self.currentSize = 0
 
    def get_node(self, index):
        current = self.first
        for i in range(index):
            current = current.next
            if current == self.first:
                return None
        return current
    
    def contains(self,element):
        temp = self.first
        while temp:
            if temp.data == element:
                return True
            temp = temp.next
        return False
    
    def getIndex(self,element):
        if self.contains(element):
            temp = self.first
            ind = 0
            while temp:
                if temp.data == element:
                   return ind
                ind+=1
                temp = temp.next
        return -1
    
    def removeAll(self, element):
        while self.contains(element):
            self.remove(self.getIndex(element))

    def get(self,index):
        return get_node(index).data
 
    def insert_after(self, ref_node, new_node): #This method is for inserting elements into the list when the user selects insert after option
        new_node.prev = ref_node
        new_node.next = ref_node.next
        new_node.next.prev = new_node
        ref_node.next = new_node
        self.currentSize+=1
 
    def insert_before(self, ref_node, new_node): #This method is for inserting elements into the list when the user selects insert before option
        self.insert_after(ref_node.prev, new_node)
 
    def insert_at_end(self, new_node): #This method is for inserting elements into the list when the user selects insert at end option
        if self.first is None:
            self.first = new_node
            new_node.next = new_node
            new_node.prev = new_node
            self.currentSize+=1
        else:
            self.insert_after(self.first.prev, new_node)
 
    def insert_at_beg(self, new_node): #This method is for inserting elements into the list when the user selects insert at beginning option
        self.insert_at_end(new_node)
        self.first = new_node
 
    def remove(self, node):	#This method is for deleting elements from the list
        if self.contains(node.data):
            temp = self.first.next
            prev = self.first

            if prev == node:
                self.first.prev.next = temp
                temp.prev = self.first.prev
                self.currentSize-=1
            while temp is not None:
                if temp.data == node.data:
                    prev.next = temp.next
                    temp.next.prev = prev
                    self.currentSize-=1
                    break
                temp = temp.next
                prev = prev.next
        return
            
    def clear(self):
        while self.currentSize is not 0:
            element = self.get_node(0)
            self.remove(element)
        self.currentSize = 0
 
    def display(self):	#This method is for showing elements present in the list
        if self.first is None:
            return
        current = self.first
        while True:
            print(current.data, end = ' ')
            current = current.next
            if current == self.first:
                break
 

