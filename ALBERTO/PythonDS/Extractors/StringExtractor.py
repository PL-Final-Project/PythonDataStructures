from KeyExtractorInterface import KeyExtractorInterface


class StringExtractor(KeyExtractorInterface):
    def getKey(self, obj: str):
        return obj
