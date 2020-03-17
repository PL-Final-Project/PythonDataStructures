from abc import abstractmethod, ABC


class QueueInterface(ABC):
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def front(self):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def enqueue(self, newdata):
        pass

    @abstractmethod
    def makeEmpty(self):
        pass


