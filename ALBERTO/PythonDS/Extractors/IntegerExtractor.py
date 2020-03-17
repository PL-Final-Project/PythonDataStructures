from KeyExtractorInterface import KeyExtractorInterface


class IntegerExtractor(KeyExtractorInterface):
    def getKey(self, obj: int):
        return obj
