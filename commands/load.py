

class Load():

    def __init__(self, index):
        self.index = int(index)

    def __repr__(self):
        return 'LOAD ' + str(self.index)

    def execute(self, cpu, ram):
        value = ram.registers[self.index][1]
        cpu.accumulator = value
        return 
        