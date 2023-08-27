import sys
import os

class SystemManager():
    
    def clearConsole(self):
         os.system("cls" if os.name == "nt" else "clear")

    def exitProgram(self):
        sys.exit()

    def validatePath(self, path):
        try:
            return os.path.exists(path)
        except IndexError:
            print("Direccion error validate.")
            sys.exit()
    
    def findFilesByExtension(self, path, ext):
        files = []
        n = 0
        try:
            for f in os.listdir(path):
                if f.endswith(ext):
                    files.append([n, f])
                    n += 1
        except IndexError:
            print("Data parse error.")
            sys.exit()
        return files