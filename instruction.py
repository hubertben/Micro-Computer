

class Instruction:

    def __init__(self, index, command):
        self.index = index
        self.command = command

    def __repr__(self):
        return 'Index ' + str(self.index) +', Command ' + str(self.command)