#Definition of the ArrayStack Data Structure.
#Coded by Andrew Gonzalez (github: andrewgonzalez4) using Python3 and Vim as text editor.
class Stack:
    #Initialization of the DS.
    def __init__(self):
        self.items = []
    #Returns if the stack is empty.
    def isEmpty(self):
        return self.items == []
    #Adds an item on top of the stack.
    def push(self, item):
        self.items.insert(0,item)
    #Removes an item from the top of the stack.
    def pop(self):
        return self.items.pop(0)
    #Prints the elements in the stack.
    def printStack(self):
        print(self.items)
