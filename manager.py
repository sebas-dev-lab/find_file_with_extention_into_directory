from store import StoreSystem
from system import SystemManager
from table import Table

class Manager(StoreSystem, SystemManager, Table):
    def __init__(self):
        super().__init__()
    
    def setInputOptions(self):
        option = None
        try:
            option = input("Seleccione 1 si desea buscar archivos de determinada extensíon o 2 para salir: ")
        except IndexError:
            print("Dato inválido.")
            self.exitProgram()
        if option != "1" and option != "2":
            self.setInputOptions()
        elif option == "2":
            self.exitProgram()
        else:
            return True
    
    def setPath(self):
        path = input("Ingrese la direccion de búsqueda: ")
        self.setDir(path)
    
    def setExtension(self):
        ext = input("Ingrese la extención de los archivos a buscar (ej: py): ")
        self.setStoreExtension(ext)
    
    def verifyPath(self):
        store = self.getStore()
        self.setDirValidate(self.validatePath(store["dir"]))
    
    def getFilesFromPath(self):
        store = self.getStore()
        self.setData(self.findFilesByExtension(store["dir"], store["ext"]))

    def getTable(self):
        store = self.getStore()
        self.setTableHeaders([f"Files with extension {store['ext']}"])
        self.setTableContent(store["data"])
        self.printTable()

    def controlFlow(self):
        opt = input("Aprete ENTER si desea realizar una nueva búsqueda o escribe -exit- para salir: ")
        if opt == "exit":
            self.exitProgram()
        elif opt != "" and opt != "exit":
            self.controlFlow()
        else:
            return True
        