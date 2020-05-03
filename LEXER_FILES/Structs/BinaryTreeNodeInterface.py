from abc import abstractmethod, ABC


class BinaryTreeNodeInterface(ABC):

    @abstractmethod
    def getValue(self):
        pass

    @abstractmethod
    def getLeftChild(self):
        pass

    @abstractmethod
    def getRightChild(self):
        pass

    @abstractmethod
    def getParent(self):
        pass
