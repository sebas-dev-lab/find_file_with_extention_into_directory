from manager import Manager

class ControlFlow:
    def __init__(self):
        self.manager = Manager()

    def execute(self):
        control = True
        while control:
            self.manager.clearConsole()
            self.manager.setInputOptions()
            self.manager.clearConsole()
            self.manager.setPath()
            self.manager.clearConsole()
            self.manager.setExtension()
            self.manager.clearConsole()
            self.manager.verifyPath()
            self.manager.getFilesFromPath()
            self.manager.clearConsole()
            self.manager.getTable()
            control = self.manager.controlFlow()