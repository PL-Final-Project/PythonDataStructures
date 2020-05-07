from Structs.BagInterface import BagInterface


class DynamicBag(BagInterface):
    def __init__(self):
        self.elements = []
        self.default_size = 10

    def size(self):
        return len(self.elements)

    def isEmpty(self):
        return len(self.elements) == 0

    def add(self, item):
        self.elements.append(item)

    def isMember(self, item):
        return item in self.elements

    def count(self, item):
        if item in self.elements:
            return self.elements[item]
        else:
            return 0

    def remove(self, item):
        self.elements.remove(item)
        return True

    def removeAll(self, item):
        result = 0
        while self.elements.remove(item):
            result += 1
        return result

    def clear(self):
        self.elements.clear()

def test():
    temo_bag = DynamicBag()
    temo_bag.add("hola")
    temo_bag.add("hola")
    temo_bag.add("hola")
    temo_bag.add("hola")
    temo_bag.add("hola")
    temo_bag.removeAll("hola")




if __name__ == '__main__':
    # main()
    test()



