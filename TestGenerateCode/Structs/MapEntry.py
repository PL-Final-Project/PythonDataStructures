class MapEntry:
    def __init__(self, key=None, value=None, status=False):
        self.key = key
        self.value = value
        self.status = status

    def isStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value