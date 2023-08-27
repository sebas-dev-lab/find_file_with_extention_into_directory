class StoreSystem:
    def __init__(self):
        self.__dir = None
        self.__extension = None
        self.__dir_validate = False
        self.__data = None
    
    def setDir(self, dir):
        self.__dir = dir
    
    def setStoreExtension(self, ext):
        self.__extension = ext

    def setDirValidate(self, validate = False):
        self.__dir_validate = validate
    
    def setData(self, data):
        self.__data = data
    
    def getStore(self):
        return {
            "dir": self.__dir,
            "ext": self.__extension,
            "dir_validate": self.__dir_validate,
            "data": self.__data
        }