from abc import abstractmethod, ABC


class BagInterface(ABC):
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def add(self, newdata):
        pass

    @abstractmethod
    def isMember(self, newdata):
        pass

    @abstractmethod
    def remove(self, newdata):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def removeAll(self, newdata):
        pass

    @abstractmethod
    def count(self, newdata):
        pass
