from Comparator import Comparator


class StringComparator(Comparator):
    def compareTo(self, a: int, b: int):
        if a == b:
            return 0
        elif a < b:
            return -1
        else:
            return 1