

class Load(command):

    def __init__(self, index):
        self.index = index

    def execute(self, ram):
        return 'load ' + str(ram[self.index])
        