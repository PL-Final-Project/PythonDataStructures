from abc import abstractmethod

class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    @abstractmethod
    def getKey(self):
        pass

    @abstractmethod
    def getValue(self):
        pass

