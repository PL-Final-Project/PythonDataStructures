from abc import ABC, abstractmethod


class Comparator(ABC):
    @abstractmethod
    def compareTo(self, a, b):
        pass
