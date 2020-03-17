from abc import abstractmethod, ABC


class KeyExtractorInterface(ABC):
    @abstractmethod
    def getKey(self, obj):
        pass
