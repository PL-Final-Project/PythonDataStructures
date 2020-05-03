from Structs.Comparator import Comparator


class NumberComparator(Comparator):
    def compareTo(self, a: int, b: int):
        if a == b:
            return 0
        elif a < b:
            return -1
        else:
            return 1