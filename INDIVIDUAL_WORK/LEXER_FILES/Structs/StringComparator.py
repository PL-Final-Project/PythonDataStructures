from Structs.Comparator import Comparator


class StringComparator(Comparator):
    def compareTo(self, a: str, b: str):
        if a == b:
            return 0
        elif a < b:
            return -1
        else:
            return 1
