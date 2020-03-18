from abc import abstractmethod, ABC


class SortedListInterface(ABC):
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def get_index(self, index):
        pass

    @abstractmethod
    def get_obj(self, obj):
        pass

    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def remove_index(self, index):
        pass

    @abstractmethod
    def remove_obj(self, obj):
        pass

    @abstractmethod
    def isMember(self, obj):
        pass

    @abstractmethod
    def firstIndexOf(self, obj):
        pass

    @abstractmethod
    def lastIndexOf(self, obj):
        pass
