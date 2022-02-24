class MockUtils:
    @staticmethod
    def generateMockData(numberCaracteres):
        return "A" * (numberCaracteres - 1) + "b"
    
    @staticmethod
    def dataLength(mock):
        return len(mock)