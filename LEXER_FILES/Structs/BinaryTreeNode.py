from .BinaryTreeNodeInterface import BinaryTreeNodeInterface


class BinaryTreeNode(BinaryTreeNodeInterface):
    def __init__(self, value=None, leftChild=None, rightChild=None, parent=None):
        self.value = value
        self.rightChild = rightChild
        self.leftChild = leftChild
        self.parent = parent

    def getValue(self):
        return self.value

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def getParent(self):
        return self.parent

    def setValue(self, value):
        self.value = value

    def setLeftChild(self, leftChild):
        self.leftChild = leftChild

    def setRightChild(self, rightChild):
        self.rightChild = rightChild

    def setValue(self, parent):
        self.parent = parent

