

class Command:

    def __init__(self, command, index):
        self.command = command
        self.index = index

    def execute(self):
        return str(self.command) + " " + str(ram[self.index])