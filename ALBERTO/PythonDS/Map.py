from abc import abstractmethod, ABC


class MapInterface(ABC):
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def linearHashFunction(self, key, arraySize) -> int:
        pass

    @abstractmethod
    def squareHashFunction(self, key, arraySize) -> int:
        pass

    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def put(self, key, value):
        pass

    @abstractmethod
    def remove(self, key):
        pass

    @abstractmethod
    def makeEmpty(self):
        pass

    @abstractmethod
    def containsKey(self, key):
        pass

    @abstractmethod
    def getKeys(self):
        pass

    @abstractmethod
    def getValues(self):
        pass
