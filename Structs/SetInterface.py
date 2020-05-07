from abc import abstractmethod, ABC


class SetInterface(ABC):
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
    def isSubset(self, newdata):
        pass

    @abstractmethod
    def union(self, newdata):
        pass

    @abstractmethod
    def difference(self, newdata):
        pass

    @abstractmethod
    def intersection(self, newdata):
        pass

    @abstractmethod
    def toArray(self):
        pass


